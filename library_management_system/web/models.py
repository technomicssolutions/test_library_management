from django.db import models


# Create your models here.
class Student(models.Model):
	Student_id  =  models.CharField('Student ID', max_length = 200, unique = True )
	Student_name = models.CharField('Student Name', max_length = 200 )
	age = models.IntegerField('Age')
	address = models.CharField('Address', max_length = 200)
	def __unicode__(self):
		return self.Student_name



class BookCategory(models.Model):
	Book_category = models.CharField('Book Category', max_length = 200)
	def __unicode__(self):
		return self.Book_category



class Book(models.Model):
	Book_id = models.CharField('Book ID', max_length = 200, unique = True)
	Book_name = models.CharField('Book Name', max_length = 200)
	def  __unicode__(self):
		return self.Book_name



class Issue(models.Model):
	student = models.ForeignKey('Student',max_length = 200)
	book = models.ForeignKey('Book', max_length = 200)
	Issue_date =  models.DateTimeField('Issue date')
	Return_date = models.DateTimeField('Return date')
	def __unicode__(self):
		return self.book.Book_name
