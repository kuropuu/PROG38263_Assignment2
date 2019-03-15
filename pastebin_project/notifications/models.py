from django.db import models
from django.urls import reverse
from home.models import Paste, UploadPaste
from django.contrib.auth.models import User
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.db.models import Q
from django.conf import settings
from django.contrib.staticfiles.urls import static

import sys, re, os

class Notifications(models.Model):
	title = models.CharField(max_length=256)
	message = models.TextField()
	viewed = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_welcome_message(sender, **kwargs):
	if kwargs.get('created', False):
		Notifications.objects.create(user=kwargs.get('instance'),
									title="Welcome to Pastebin Clone!",
									message="Thanks for signing up for our website! We hope you enjoy sharing pastes with your friends and colleagues. Please don't hesitate to reach out to one of the admins if you need any help :)")

@receiver(m2m_changed, sender=Paste.invited_users.through)
def invited_to_paste_message(sender, instance, action, **kwargs):
	if action == "post_add":
		all_users = instance.invited_users.all()
		paste_slug = instance.slug
		for i in all_users:
			Notifications.objects.create(user=i,
						     title="Invitation to Paste",
						     message="You've been invited to view a paste! Click <a href=\"/paste/%s\">here</a> for the link." %paste_slug)

@receiver(m2m_changed, sender=UploadPaste.invited_users.through)
def invited_to_upload_message(sender, instance, action, **kwargs):
	if action == "post_add":
		all_users = instance.invited_users.all()
		paste_slug = instance.slug
		for i in all_users:
			Notifications.objects.create(user=i,
						     title="Invitation to Uploaded Paste",
						     message="You've been invited to view an uploaded paste! Click <a href=\"/paste/upload/%s\">here</a> for the link." %paste_slug)

# For keyword notifications
class Keywords(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	keyword1 = models.CharField(max_length=50, null=True, blank=True, default=None)
	keyword2 = models.CharField(max_length=50, null=True, blank=True, default=None)
	keyword3 = models.CharField(max_length=50, null=True, blank=True, default=None)

	def get_absolute_url(self):
		return reverse('profile')

@receiver(post_save, sender=Paste)
def keyword_notification_message(sender, **kwargs):
	if kwargs.get('created', False):
		paste = kwargs.get('instance')

		for i in Keywords.objects.all():
			if i.keyword1 is not None:
				if re.search(i.keyword1, paste.title) or re.search(i.keyword1, paste.content):
					Notifications.objects.create(user=User.objects.get(id=i.user_id), 
						title="Keyword Match Found",
						message="A new paste was just created with a keyword you specified. Click <a href=\"/paste/%s\">here</a> for the link." %paste.slug)
			if i.keyword2 is not None:
				if re.search(i.keyword2, paste.title) or re.search(i.keyword2, paste.content):
					Notifications.objects.create(user=User.objects.get(id=i.user_id), 
						title="Keyword Match Found",
						message="A new paste was just created with a keyword you specified. Click <a href=\"/paste/%s\">here</a> for the link." %paste.slug)
			if i.keyword3 is not None:
				if re.search(i.keyword3, paste.title) or re.search(i.keyword3, paste.content):
					Notifications.objects.create(user=User.objects.get(id=i.user_id),
					 title="Keyword Match Found",
					 message="A new paste was just created with a keyword you specified. Click <a href=\"/paste/%s\">here</a> for the link." %paste.slug)


@receiver(post_save, sender=UploadPaste)
def upload_keyword_notification_message(sender, **kwargs):
	# define base directory
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	paste = kwargs.get('instance')
	
	# define the path to find the uploaded file
	file_path = os.path.join(BASE_DIR, 'uploads/')+'%s' %paste.content

	if kwargs.get('created', False):
		for i in Keywords.objects.all():
			with open(file_path, "r") as text:
				for line in text:
					if i.keyword1 is not None:
						if re.search(i.keyword1, line) or re.search(i.keyword1, line):
							Notifications.objects.create(user=User.objects.get(id=i.user_id), 
								title="Keyword Match Found",
								message="A new paste was just created with a keyword you specified. Click <a href=\"/paste/upload/%s\">here</a> for the link." %paste.slug)
					if i.keyword2 is not None:
						if re.search(i.keyword2, line) or re.search(i.keyword2, line):
							Notifications.objects.create(user=User.objects.get(id=i.user_id), 
								title="Keyword Match Found",
								message="A new paste was just created with a keyword you specified. Click <a href=\"/paste/upload/%s\">here</a> for the link." %paste.slug)
					if i.keyword3 is not None:
						if re.search(i.keyword3, line) or re.search(i.keyword3, line):
							Notifications.objects.create(user=User.objects.get(id=i.user_id),
							 title="Keyword Match Found",
							 message="A new paste was just created with a keyword you specified. Click <a href=\"/paste/upload/%s\">here</a> for the link." %paste.slug)

