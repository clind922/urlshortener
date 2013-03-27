# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Word.used'
        db.add_column(u'urlshortener_word', 'used',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Word.used'
        db.delete_column(u'urlshortener_word', 'used')


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
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        }
    }

    complete_apps = ['urlshortener']