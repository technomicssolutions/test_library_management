# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Issue.Issue_date'
        db.delete_column(u'web_issue', 'Issue_date')

        # Deleting field 'Issue.Return_date'
        db.delete_column(u'web_issue', 'Return_date')

        # Adding field 'Issue.issue_date'
        db.add_column(u'web_issue', 'issue_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Issue.return_date'
        db.add_column(u'web_issue', 'return_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Student.Student_name'
        db.delete_column(u'web_student', 'Student_name')

        # Deleting field 'Student.Student_id'
        db.delete_column(u'web_student', 'Student_id')

        # Adding field 'Student.student_id'
        db.add_column(u'web_student', 'student_id',
                      self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.student_name'
        db.add_column(u'web_student', 'student_name',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'BookCategory.Book_category'
        db.delete_column(u'web_bookcategory', 'Book_category')

        # Adding field 'BookCategory.book_category'
        db.add_column(u'web_bookcategory', 'book_category',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Book.Issue_date'
        db.delete_column(u'web_book', 'Issue_date')

        # Deleting field 'Book.Book_name'
        db.delete_column(u'web_book', 'Book_name')

        # Deleting field 'Book.Book_category'
        db.delete_column(u'web_book', 'Book_category_id')

        # Deleting field 'Book.Book_id'
        db.delete_column(u'web_book', 'Book_id')

        # Deleting field 'Book.Return_date'
        db.delete_column(u'web_book', 'Return_date')

        # Adding field 'Book.book_id'
        db.add_column(u'web_book', 'book_id',
                      self.gf('django.db.models.fields.CharField')(max_length=200, unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Book.book_name'
        db.add_column(u'web_book', 'book_name',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Book.book_category'
        db.add_column(u'web_book', 'book_category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.BookCategory'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Book.issue_date'
        db.add_column(u'web_book', 'issue_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Book.return_date'
        db.add_column(u'web_book', 'return_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Issue.Issue_date'
        raise RuntimeError("Cannot reverse this migration. 'Issue.Issue_date' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Issue.Return_date'
        raise RuntimeError("Cannot reverse this migration. 'Issue.Return_date' and its values cannot be restored.")
        # Deleting field 'Issue.issue_date'
        db.delete_column(u'web_issue', 'issue_date')

        # Deleting field 'Issue.return_date'
        db.delete_column(u'web_issue', 'return_date')


        # User chose to not deal with backwards NULL issues for 'Student.Student_name'
        raise RuntimeError("Cannot reverse this migration. 'Student.Student_name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Student.Student_id'
        raise RuntimeError("Cannot reverse this migration. 'Student.Student_id' and its values cannot be restored.")
        # Deleting field 'Student.student_id'
        db.delete_column(u'web_student', 'student_id')

        # Deleting field 'Student.student_name'
        db.delete_column(u'web_student', 'student_name')


        # User chose to not deal with backwards NULL issues for 'BookCategory.Book_category'
        raise RuntimeError("Cannot reverse this migration. 'BookCategory.Book_category' and its values cannot be restored.")
        # Deleting field 'BookCategory.book_category'
        db.delete_column(u'web_bookcategory', 'book_category')

        # Adding field 'Book.Issue_date'
        db.add_column(u'web_book', 'Issue_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Book.Book_name'
        raise RuntimeError("Cannot reverse this migration. 'Book.Book_name' and its values cannot be restored.")
        # Adding field 'Book.Book_category'
        db.add_column(u'web_book', 'Book_category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web.BookCategory'], null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Book.Book_id'
        raise RuntimeError("Cannot reverse this migration. 'Book.Book_id' and its values cannot be restored.")
        # Adding field 'Book.Return_date'
        db.add_column(u'web_book', 'Return_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Book.book_id'
        db.delete_column(u'web_book', 'book_id')

        # Deleting field 'Book.book_name'
        db.delete_column(u'web_book', 'book_name')

        # Deleting field 'Book.book_category'
        db.delete_column(u'web_book', 'book_category_id')

        # Deleting field 'Book.issue_date'
        db.delete_column(u'web_book', 'issue_date')

        # Deleting field 'Book.return_date'
        db.delete_column(u'web_book', 'return_date')

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
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Book']", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'return_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web.Student']", 'max_length': '200'})
        },
        u'web.student': {
            'Meta': {'object_name': 'Student'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'books_in_hand': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fine': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'student_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['web']