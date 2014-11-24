# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ArticleType'
        db.create_table(u'blog_articletype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
        ))
        db.send_create_signal(u'blog', ['ArticleType'])

        # Adding model 'Article'
        db.create_table(u'blog_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.ArticleType'])),
        ))
        db.send_create_signal(u'blog', ['Article'])

        # Adding model 'Like'
        db.create_table(u'blog_like', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Article'])),
        ))
        db.send_create_signal(u'blog', ['Like'])

        # Adding model 'Comment'
        db.create_table(u'blog_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Article'])),
        ))
        db.send_create_signal(u'blog', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'ArticleType'
        db.delete_table(u'blog_articletype')

        # Deleting model 'Article'
        db.delete_table(u'blog_article')

        # Deleting model 'Like'
        db.delete_table(u'blog_like')

        # Deleting model 'Comment'
        db.delete_table(u'blog_comment')


    models = {
        u'blog.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.ArticleType']"})
        },
        u'blog.articletype': {
            'Meta': {'object_name': 'ArticleType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        u'blog.comment': {
            'Meta': {'object_name': 'Comment'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Article']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'blog.like': {
            'Meta': {'object_name': 'Like'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Article']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['blog']