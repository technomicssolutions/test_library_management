# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Student.age'
        db.alter_column(u'web_student', 'age', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Student.books_in_hand'
        db.alter_column(u'web_student', 'books_in_hand', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Student.address'
        db.alter_column(u'web_student', 'address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Student.fine'
        db.alter_column(u'web_student', 'fine', self.gf('django.db.models.fields.IntegerField')(null=True))
    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Student.age'
        raise RuntimeError("Cannot reverse this migration. 'Student.age' and its values cannot be restored.")

        # Changing field 'Student.books_in_hand'
        db.alter_column(u'web_student', 'books_in_hand', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Student.address'
        raise RuntimeError("Cannot reverse this migration. 'Student.address' and its values cannot be restored.")

        # Changing field 'Student.fine'
        db.alter_column(u'web_student', 'fine', self.gf('django.db.models.fields.IntegerField')())
    models = {
        u'web.book': {
            'Meta': {'object_name': 'Book'},
            'book_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.BookCategory']", 'null': 'True', 'blank': 'True'}),
            'book_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'book_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'return_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'web.bookcategory': {
            'Meta': {'object_name': 'BookCategory'},
            'book_category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'web.issue': {
            'Meta': {'object_name': 'Issue'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '200', 'to': u"orm['web.Book']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'return_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '200', 'to': u"orm['web.Student']", 'null': 'True', 'blank': 'True'})
        },
        u'web.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'books_in_hand': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'fine': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'student_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['web']