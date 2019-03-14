from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

privacy_choices = (
	('Private', 'Private'),
	('Public', 'Public'),
)

status_choices = (
	('Enabled', 'Enabled'),
	('Disabled', 'Disabled'),
)

class Paste(models.Model):
	category = models.CharField(max_length=10, default='paste')
	privacy = models.CharField(choices=privacy_choices, max_length=10, default='Private')
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE,
		related_name='%(class)s_requests_created')
	invited_users = models.ManyToManyField(User, blank=True)
	status = models.CharField(choices=status_choices, max_length=10, default='Enabled')
	expiry = models.DateField(default=timezone.now, null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('paste-detail', kwargs={'pk': self.pk})

class UploadPaste(models.Model):
	category = models.CharField(max_length=10, default='uploadpaste')
	privacy = models.CharField(choices=privacy_choices, max_length=10, default='Private')
	title = models.CharField(max_length=100)
	content = models.FileField(upload_to='.')
	date_posted = models.DateTimeField(default=timezone.now)
	creator = models.ForeignKey(User, on_delete=models.CASCADE,
		related_name='%(class)s_requests_created')
	invited_users = models.ManyToManyField(User, blank=True)
	status = models.CharField(choices=status_choices, max_length=10, default='Enabled')
	expiry = models.DateField(default=timezone.now, null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('paste-detail', kwargs={'pk': self.pk})
