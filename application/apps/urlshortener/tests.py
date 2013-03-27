from django.test import TestCase, Client
from application.apps.urlshortener.models import Word, ShortURL
from application.apps.urlshortener.views import parse_url_words


class TestShortURL(TestCase):

    def test_extract_url_words(self):
        """
        Text extract word from url
        """
        url = 'http://www.test-blog.com/12/11/10/test_word-ASDF-in-a-url-slug-4th'

        words = parse_url_words(url)

        print words

        self.failUnless(len(words) == 12)

    def test_submit_url(self):
        for word in ['test', 'abc', 'dn']:
            Word.objects.create(word=word)

        c = Client()
        # Test a simple URL
        response = c.post('/', {'redirect_url': 'http://www.test.se/'})
        self.assertEqual(response.status_code, 302)

        obj = ShortURL.objects.all().order_by('-created')[0]
        self.assertEqual(obj.url_key.word, 'test')

        # Test same URL again
        response = c.post('/', {'redirect_url': 'http://www.test.se/'})
        self.assertEqual(response.status_code, 302)

        obj = ShortURL.objects.all().order_by('-created')[0]
        self.failUnless(obj.url_key.word in ['abc', 'dn'])



