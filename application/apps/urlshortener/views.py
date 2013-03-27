# Create your views here.
import random
import re
from django.utils.translation import ugettext_lazy as _
from django.http.response import HttpResponseRedirect
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from application.apps.urlshortener.forms import ShortURLForm
from application.apps.urlshortener.models import ShortURL, Word


def parse_url_words(url):
    words = re.findall('\w+', url.lower())
    # Todo: Maybe filter out fully numeric words

    # Filter out some unsuitable words
    return [word for word in words if word not in ['http', 'www', 'com','org','net']]


class ShortURLCreateView(CreateView):
    """
    View used to create new URL redirects
    """
    form_class = ShortURLForm
    model = ShortURL

    def form_valid(self, form):
        words = parse_url_words(form.instance.redirect_url)
        word = None
        # Look up in the database if any of the words exist
        if len(words):
            matching_words = Word.objects.filter(word__in=words, used=False)

            # If we found at least one word, use it and set it as used
            if matching_words.exists():
                word = matching_words[0].word
        # No word could be found, select a random one
        if not word:
            available_words = Word.objects.filter(used=False)
            # If at least one available word exits
            if available_words.exists():
                word = random.choice(available_words).word
            else:  # No available words, delete the first created redirect and use its word
                url = ShortURL.objects.all().order_by('-created')[0]
                url.url_key.used = False
                url.url_key.save()
                url.delete()
                word = Word.objects.filter(used=False)[0].word
        # Select it manually to get an actual reference
        matching_word = Word.objects.get(word=word)
        matching_word.used = True
        matching_word.save()
        form.instance.url_key = matching_word
        self.object = form.save()

        # Redirect to view the shortened URL
        return HttpResponseRedirect(self.object.get_absolute_url())


class ShortURLRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, **kwargs):
        """
        Return the URL redirect to.
        """
        word = self.kwargs.get('slug', None)

        obj = ShortURL.objects.get(url_key__word=word)
        obj.visit()

        return obj.redirect_url


class ShortURLView(DetailView):
    template_name = 'urlshortener/shorturl_view.html'
    model = ShortURL

    def get_object(self, queryset=None):
        word = self.kwargs.get('slug', None)
        return self.model.objects.get(url_key__word=word)


class ShortURLStatsView(DetailView):
    template_name = 'urlshortener/shorturl_stats.html'
    model = ShortURL

    def get_object(self, queryset=None):
        word = self.kwargs.get('slug', None)
        return self.model.objects.get(url_key__word=word)
