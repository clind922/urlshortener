from django.core.urlresolvers import reverse
from django.db import models


class ShortURL(models.Model):
    """
    The url redirect class
    """
    url_key = models.ForeignKey('Word', unique=True, related_name='short_url')
    redirect_url = models.URLField()
    visits = models.PositiveIntegerField(default=0)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def visit(self):
        self.visits += 1
        self.save()

    def get_absolute_url(self):
        return reverse('urlshortener:view_short_url', kwargs={'slug': self.url_key.word})

    def __unicode__(self):
        return self.redirect_url


class Word(models.Model):
    """
    A class for available words
    """
    word = models.CharField(max_length=32, unique=True)
    used = models.BooleanField(default=False)

    def __unicode__(self):
        return self.word