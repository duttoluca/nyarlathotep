from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    #other user fields
    URL = models.URLField(help_text="Sito web", blank=True, null=True,)
    birth = models.DateField(help_text="Data di nascita", blank=True, null=True, verbose_name="Data di nascita")
    bio = models.TextField(help_text="Qualcosa su di te...", blank=True, null=True, verbose_name="Bio")


# signals
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
