from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	allowed_to_commit = models.BooleanField(default=False)
	is_waiting = models.BooleanField(default=False)
	date_since_waiting = models.DateTimeField(null=True)
	date_since_commiting = models.DateTimeField(null=True)

	def __str__(self):
		return self.user.first_name

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()
