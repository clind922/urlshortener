# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from application.apps.urlshortener.models import Word
import re


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Loads a word file and performs cleanup, and inserts them into the database
        """

        filename = './application/files/words.txt'
        self.stdout.write('Opening words file...\n')
        f = open(filename, 'rb')
        words = f.readlines()
        regex = re.compile('[^\w]|_+')
        unique_words = []

        self.stdout.write('Deleting...\n')
        Word.objects.all().delete()

        self.stdout.write('Starting clean and insert...\n')
        for word in words:
            word = regex.sub('', word).lower()
            if word not in unique_words:
                Word.objects.create(word=word)
                unique_words.append(word)

        # Todo: Maybe use bulk_create()

        self.stdout.write('Cleaned %s words!\n' % len(unique_words))