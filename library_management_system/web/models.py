from django.utils import timezone
from django.db import models
import datetime
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS



choices = (
    ('Male','Male'),
    ('Female','Female'),
    )
# Create your models here.
class Student(models.Model):
    student_id  =  models.CharField('Student ID', max_length = 200, unique = True, null = True, blank = True)
    student_name = models.CharField('Student Name', max_length = 200, null = True, blank = True)
    age = models.IntegerField('Age', null = True, blank = True)
    address = models.CharField('Address', max_length = 200, null = True, blank = True)
    gender = models.CharField(max_length = 10, choices = choices, null = True, blank = True)
    books_in_hand = models.IntegerField(default = 0, null = True, blank = True)
    fine = models.IntegerField(default = 0, null = True, blank = True)
    

    class Meta:
        verbose_name_plural = "Student"
            
    
    def __unicode__(self):
        return self.student_name



class BookCategory(models.Model):
    book_category = models.CharField('Book Category', max_length = 200, unique = True, null = True, blank = True)

    class Meta:
        verbose_name_plural = "Book Category"

    def __unicode__(self):
        return self.book_category



class Book(models.Model):
    book_id = models.CharField('Book ID', max_length = 200, unique = True,  null = True, blank = True)
    book_name = models.CharField('Book Name', max_length = 200,  null = True, blank = True)
    book_category = models.ForeignKey(BookCategory, null = True, blank = True)
    issue_date =  models.DateTimeField('Issued Date', null = True, blank = True)
    return_date = models.DateTimeField('Returning Date', null = True, blank = True)

    class Meta:
        verbose_name_plural = "Book"
            
    def  __unicode__(self):
        return self.book_name



class Issue(models.Model):
    student = models.ForeignKey(Student,max_length = 200 ,  null = True, blank = True)
    book = models.ForeignKey(Book, max_length = 200,  null = True, blank = True)
    issue_date =  models.DateTimeField('Issue date', null = True, blank = True)
    return_date = models.DateTimeField('Return date', null = True, blank = True)

    class Meta:
        verbose_name_plural = "Issue"
            

    def __unicode__(self):
        return self.book.book_name


