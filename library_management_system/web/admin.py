from django.contrib  import admin

from library_management_app.models  import Student, BookCategory, Book, Issue

admin.site.register(Student)
admin.site.register(BookCategory)
admin.site.register(Book)
admin.site.register(Issue)


