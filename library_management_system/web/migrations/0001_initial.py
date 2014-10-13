# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Student'
        db.create_table(u'web_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Student_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('Student_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('books_in_hand', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fine', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'web', ['Student'])

        # Adding model 'BookCategory'
        db.create_table(u'web_bookcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Book_category', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'web', ['BookCategory'])

        # Adding model 'Book'
        db.create_table(u'web_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Book_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('Book_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Book_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.BookCategory'], null=True, blank=True)),
            ('Issue_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Return_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'web', ['Book'])

        # Adding model 'Issue'
        db.create_table(u'web_issue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Student'], max_length=200)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.Book'], max_length=200)),
            ('Issue_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('Return_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'web', ['Issue'])

    def backwards(self, orm):
        # Deleting model 'Student'
        db.delete_table(u'web_student')

        # Deleting model 'BookCategory'
        db.delete_table(u'web_bookcategory')

        # Deleting model 'Book'
        db.delete_table(u'web_book')

        # Deleting model 'Issue'
        db.delete_table(u'web_issue')

    models = {
        u'web.book': {
            'Book_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.BookCategory']", 'null': 'True', 'blank': 'True'}),
            'Book_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'Book_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Issue_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Book'},
            'Return_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.bookcategory': {
            'Book_category': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'BookCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.issue': {
            'Issue_date': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'Issue'},
            'Return_date': ('django.db.models.fields.DateTimeField', [], {}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Book']", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Student']", 'max_length': '200'})
        },
        u'web.student': {
            'Meta': {'object_name': 'Student'},
            'Student_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'Student_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'books_in_hand': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fine': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['web']