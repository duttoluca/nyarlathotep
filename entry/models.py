import datetime

from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
from django.db.models import permalink


class PostManager(models.Manager):
    def get_visible(self):
        return self.get_query_set().filter(publish_at__lte=datetime.datetime.now(),
                                           active=True)


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False,
                                 help_text="Controlla se il post e' visibile.")
    publish_at = models.DateTimeField(default=datetime.datetime.now(),
                                      help_text="Quando il post sara' visibile.")
    title = models.CharField(max_length=255,
                             help_text="Titolo del post.")
    slug = models.SlugField()
    body = models.TextField()
    author = models.ForeignKey(User, related_name="posts", blank=True, null=True)

    objects = PostManager()
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return("post", (), {"slug": self.slug})

    class Meta:
        ordering = ['-publish_at', '-modified', '-created']
