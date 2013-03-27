# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ShortURL'
        db.create_table(u'urlshortener_shorturl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url_key', self.gf('django.db.models.fields.related.ForeignKey')(related_name='short_url', unique=True, to=orm['urlshortener.Word'])),
            ('redirect_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('visits', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'urlshortener', ['ShortURL'])

        # Adding model 'Word'
        db.create_table(u'urlshortener_word', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal(u'urlshortener', ['Word'])


    def backwards(self, orm):
        # Deleting model 'ShortURL'
        db.delete_table(u'urlshortener_shorturl')

        # Deleting model 'Word'
        db.delete_table(u'urlshortener_word')


    models = {
        u'urlshortener.shorturl': {
            'Meta': {'object_name': 'ShortURL'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'redirect_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url_key': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'short_url'", 'unique': 'True', 'to': u"orm['urlshortener.Word']"}),
            'visits': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'urlshortener.word': {
            'Meta': {'object_name': 'Word'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        }
    }

    complete_apps = ['urlshortener']