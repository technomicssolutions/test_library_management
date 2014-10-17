from django import forms
from django.forms import ModelForm
import datetime
from datetime import datetime
from django.utils import timezone
from web.models import Student


choices = (
    ('Select','Select'),
    ('Male','Male'),
    ('Female','Female'),
    )

class StudentForm(forms.Form):
    student_id  =  forms.CharField(max_length = 200, required = True)
    student_name = forms.CharField(max_length = 200, required = True)
    age =  forms.IntegerField(required = True)
    address =  forms.CharField(max_length = 200, required = True)
    gender =  forms.ChoiceField(choices = choices, required = True)
    books_in_hand =  forms.IntegerField(required = False)
    fine =  forms.IntegerField(required = False)
    class Meta:
        model = Student
            
            
class BookCategoriesForm(forms.Form):
    book_category = forms.CharField(max_length = 200)

class BookForm(forms.Form):
    book_id = forms.CharField(max_length = 200)
    book_name = forms.CharField( max_length = 200)
    issue_date =  forms.DateTimeField(required = True)
    return_date = forms.DateTimeField(required = True)
        
