import datetime

from django.db import models
from django.contrib.auth.models import User

from django.db.models import permalink


class Category(models.Model):
    name = models.CharField(max_length=255,
                             help_text="Nome della categoria.",
                             verbose_name="Nome")
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True,
                                 help_text="Controlla se la categoria e' visibile.",
                                 verbose_name="Categoria abilitata")


    @permalink
    def get_absolute_url(self):
        return("category", (), {"slug": self.slug})

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorie'


class PostManager(models.Manager):
    def get_visible(self):
        return self.get_query_set().filter(publish_at__lte=datetime.datetime.now(),
                                           active=True)


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False,
                                 help_text="Controlla se il post e' visibile.",
                                 verbose_name="Visualizza post")
    enable_comments = models.BooleanField(default=True,
                                          help_text="Controlla se sono permessi commenti.",
                                          verbose_name="Abilita commenti")
    publish_at = models.DateTimeField(default=datetime.datetime.now(),
                                      help_text="Quando il post sara' visibile.",
                                      verbose_name="Data pubblicazione")
    title = models.CharField(max_length=255,
                             help_text="Titolo del post.",
                             verbose_name="Titolo")
    slug = models.SlugField(unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, related_name="posts", blank=True, null=True)
    objects = PostManager()
    categories = models.ManyToManyField(Category, blank=True, null=True)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return("post", (), {"slug": self.slug})

    class Meta:
        ordering = ['-publish_at', '-modified', '-created']
