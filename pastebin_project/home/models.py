from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now, localtime
from django.db.models.signals import pre_save
from django.utils.text import slugify
import random, string
from celery.schedules import crontab
from celery.task import periodic_task
from django.core.validators import FileExtensionValidator

privacy_choices = (
	('Private', 'Private'),
	('Public', 'Public'),
)

status_choices = (
	('Enabled', 'Enabled'),
	('Disabled', 'Disabled'),
)

class Paste(models.Model):
	slug = models.SlugField(max_length=6, unique=True)
	privacy = models.CharField(choices=privacy_choices, max_length=10, default='Private')
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE,
		related_name='%(class)s_requests_created')
	invited_users = models.ManyToManyField(User, blank=True)
	status = models.CharField(choices=status_choices, max_length=10, default='Enabled')
	expiry = models.DateField(null=True, blank=True)
	expired = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('paste-detail', kwargs={'slug': self.slug})

	@property
	@periodic_task(run_every=crontab(hour=0, minute=0))
	def expired(self):
		if self.expiry is not None:
			return self.expiry <= localtime(now()).date()


class UploadPaste(models.Model):
	slug = models.SlugField(max_length=6, unique=True)
	privacy = models.CharField(choices=privacy_choices, max_length=10, default='Private')
	title = models.CharField(max_length=100)
	content = models.FileField(upload_to='./txtfiles/', validators=[FileExtensionValidator(['txt'])])
	date_posted = models.DateTimeField(default=timezone.now)
	creator = models.ForeignKey(User, on_delete=models.CASCADE,
		related_name='%(class)s_requests_created')
	invited_users = models.ManyToManyField(User, blank=True)
	status = models.CharField(choices=status_choices, max_length=10, default='Enabled')
	expiry = models.DateField(null=True, blank=True)
	expired = models.BooleanField(default=False)
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('upload_detail', kwargs={'slug': self.slug})

	@property
	@periodic_task(run_every=crontab(hour=0, minute=0))
	def expired(self):
		if self.expiry is not None:
			return self.expiry <= localtime(now()).date()

def create_slug(instance, new_slug=None):
	random_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(6))
	slug = slugify(random_string)
	if new_slug is not None:
		slug = new_slug
	queryset = Paste.objects.filter(slug=slug).order_by("-id")
	queryset2 = UploadPaste.objects.filter(slug=slug).order_by("-id")

	exists = queryset.exists()
	exists2 = queryset2.exists()
	if exists:
		new_slug = "%s-%s" %(slug, queryset.first().id)
		return create_slug(instance, new_slug=new_slug)
	elif exists2:
		new_slug = "%s-%s" %(slug, queryset2.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug	

def pre_save_paste_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_paste_receiver, sender=Paste)
pre_save.connect(pre_save_paste_receiver, sender=UploadPaste)
