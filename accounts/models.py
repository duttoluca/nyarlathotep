from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    #other user fields
    URL = models.URLField(help_text="Sito web", blank=True)
    birth = models.DateField(help_text="Data di nascita", blank=True)