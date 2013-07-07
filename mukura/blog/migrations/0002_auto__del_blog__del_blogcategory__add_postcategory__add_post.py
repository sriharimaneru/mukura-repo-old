# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table('blog_blog')

        # Removing M2M table for field category on 'Blog'
        db.delete_table('blog_blog_category')

        # Deleting model 'BlogCategory'
        db.delete_table('blog_blogcategory')

        # Adding model 'PostCategory'
        db.create_table('blog_postcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('blog', ['PostCategory'])

        # Adding model 'Post'
        db.create_table('blog_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('time_stamp', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('blog', ['Post'])

        # Adding M2M table for field category on 'Post'
        db.create_table('blog_post_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('postcategory', models.ForeignKey(orm['blog.postcategory'], null=False))
        ))
        db.create_unique('blog_post_category', ['post_id', 'postcategory_id'])


    def backwards(self, orm):
        # Adding model 'Blog'
        db.create_table('blog_blog', (
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('time_stamp', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal('blog', ['Blog'])

        # Adding M2M table for field category on 'Blog'
        db.create_table('blog_blog_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm['blog.blog'], null=False)),
            ('blogcategory', models.ForeignKey(orm['blog.blogcategory'], null=False))
        ))
        db.create_unique('blog_blog_category', ['blog_id', 'blogcategory_id'])

        # Adding model 'BlogCategory'
        db.create_table('blog_blogcategory', (
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('blog', ['BlogCategory'])

        # Deleting model 'PostCategory'
        db.delete_table('blog_postcategory')

        # Deleting model 'Post'
        db.delete_table('blog_post')

        # Removing M2M table for field category on 'Post'
        db.delete_table('blog_post_category')


    models = {
        'blog.post': {
            'Meta': {'object_name': 'Post'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.PostCategory']", 'symmetrical': 'False'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'time_stamp': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'blog.postcategory': {
            'Meta': {'object_name': 'PostCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['blog']