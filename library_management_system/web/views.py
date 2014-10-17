# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,render_to_response
from django.views import generic
from web.models  import Student, BookCategory, Book, Issue
from web.forms import StudentForm,BookCategoriesForm,BookForm
from django.views.generic.base import View
from datetime import datetime
from django.utils import timezone
import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate


def home(request):
    return render(request, 'web/home.html', {})

class StudentView(generic.ListView):
    template_name = 'web/students.html'
    context_object_name = 'latest_student_list'
    def get_queryset(self):
        return Student.objects.order_by('student_name')

class BookCategoryView(generic.ListView):
    template_name = 'web/book_category.html'
    context_object_name = 'latest_bookcategories_list'
    def get_queryset(self):
        return BookCategory.objects.order_by('book_category')


class BookView(generic.ListView):
    template_name = 'web/books.html'
    context_object_name = 'latest_book_list'
    def get_queryset(self):
        return Book.objects.order_by('book_name')



def create_student(request):
    
    if request.method == 'GET':
        form = StudentForm()
    else :
        form = StudentForm(request.POST)

        if form.is_valid():
            student_data = form.cleaned_data
            print student_data
            student = Student() 

            student.student_id = student_data['student_id']
            student.student_name = student_data['student_name']
            student.age = student_data['age']
            student.address = student_data['address']
            student.gender = student_data['gender']
            student.books_in_hand = student_data['books_in_hand']
            student.fine = student_data['fine']
            student.save()

            return HttpResponseRedirect(reverse('students'))
        else :
            form = StudentForm(request.POST)
    return render(request, 'web/create_student.html', {'form': form})



def create_bookcategory(request):
    if request.method == 'GET':
        form = BookCategoriesForm()
    else:
        form = BookCategoriesForm(request.POST)
        if form.is_valid():
            bookcategory_data = form.cleaned_data
            print bookcategory_data
            bookcategory = BookCategory()
            bookcategory.book_category = bookcategory_data['book_category']
            bookcategory.save()

            return HttpResponseRedirect(reverse('bookcategories'))
        else:
            form = BookCategoriesForm(request.POST)
    return render(request, 'web/create_bookcategory.html', {'form': form})



def create_book(request):
    book_categories = BookCategory.objects.all()
    print 'book_categories', book_categories
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(request.POST)
        
        if form.is_valid():
            book_data = form.cleaned_data
            print book_data
            book = Book()
            book.book_id = book_data['book_id']
            book.book_name = book_data['book_name']
            book.book_category = BookCategory.objects.get(id=request.POST['book_category'])
            book.issue_date = book_data['issue_date']
            book.return_date = book_data['return_date']
            book.save()
            
           
            return HttpResponseRedirect(reverse('books'))
        else:
            form = BookForm(request.POST)
        
    context = {
        'book_categories' : book_categories,
        'form': form
    }
    return render(request, 'web/create_book.html', context)




def edit_student(request, student_id):
    
    student = Student.objects.get(id=student_id)
    print 'student', student
    student_data = {
        'student_id' : student.student_id,
        'student_name': student.student_name,
        'age' : student.age,
        'address' : student.address,
        'gender' : student.gender,
        'books_in_hand' : student.books_in_hand,
        'fine' : student.fine,

    }
    print "request", request.method
    if request.method == 'GET':
        form = StudentForm(initial = student_data)
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            print "is_valid"
            student_data = form.cleaned_data
            print student_data
            student.student_id = student_data['student_id']
            student.student_name = student_data['student_name']
            student.age = student_data['age']
            student.address = student_data['address']
            student.gender = student_data['gender']
            student.books_in_hand = student_data['books_in_hand']
            student.fine = student_data['fine']
            student.save()

            return HttpResponseRedirect(reverse('students'))
        else:
            print "in else"
            form = StudentForm(request.POST)
    return render(request, 'web/edit_student.html', {'form': form, 'student': student})


def edit_bookcategory(request, bookcategory_id):
    
    bookcategory = BookCategory.objects.get(id=bookcategory_id)
    print 'book category',bookcategory

    bookcategory_data = {
        'book_category' : bookcategory.book_category,
        
    }

    print "request", request.method
    if request.method == 'GET':
        form = BookCategoriesForm(initial = bookcategory_data)
    else:
        form = BookCategoriesForm(request.POST)
        if form.is_valid():
            print "is_valid"
            bookcategory_data = form.cleaned_data
            print bookcategory_data
            bookcategory.book_category = bookcategory_data['book_category']
            
            bookcategory.save()

            return HttpResponseRedirect(reverse('bookcategories'))
        else:
            print "in else"
            form = BookCategoriesForm(request.POST)
    return render(request, 'web/edit_bookcategory.html', {'form': form, 'book_category' : bookcategory})



def edit_book(request, book_id):
    
    book = Book.objects.get(id=book_id)
    print 'book' , book
    book_data = {

        'book_id' : book.book_id,
        'book_name': book.book_name,
        'issue_date' : book.issue_date,
        'return_date' : book.return_date
        

    }
    print "request", request.method
    if request.method == 'GET':
        form = BookForm(initial = book_data)
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            print "is_valid"
            book_data = form.cleaned_data
            print book_data
            book.book_id = book_data['book_id']
            book.book_name = book_data['book_name']
            book.issue_date = book_data['issue_date']
            book.return_date = book_data['return_date']
            
            book.save()

            return HttpResponseRedirect(reverse('books'))

        else:

            print "in else"

            form = BookForm(request.POST)

    return render(request, 'web/edit_book.html', {'form': form, 'book': book})



def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return HttpResponseRedirect(reverse('books'))


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return HttpResponseRedirect(reverse('students'))

def delete_bookcategory(request, bookcategory_id):
    bookcategory = BookCategory.objects.get(id=bookcategory_id)
    bookcategory.delete()
    return HttpResponseRedirect(reverse('bookcategories'))








    








