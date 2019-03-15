from django.db import models
from home.models import Paste
from django.contrib.auth.models import User
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

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
									message="Thanks for signing up for our website! We hope you enjoy sharaing pastes with your friends and colleagues. Please don't hesitate to reach out to one of the admins if you need any help :)")

@receiver(m2m_changed, sender=Paste.invited_users.through)
def invited_to_paste_message(sender, instance, action, **kwargs):
	if action == "post_add":
		all_users=instance.invited_users.all()
		for i in all_users:
			Notifications.objects.create(user=i,
										 title="Invitation to Paste",
										 message="You've been invited to view a paste! Please check the homepage.")
		