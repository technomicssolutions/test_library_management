from django.conf.urls  import patterns,url
from web import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'library_management_system.views.home', name='home'),
    # url(r'^library_management_system/', include('library_management_system.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
	
	url(r'^$', views.home, name = 'home'),
	url(r'^students/$', views.StudentView.as_view(), name = 'students'),
	url(r'^book_category/$', views.BookCategoryView.as_view(), name = 'bookcategories'),
	url(r'^books/$', views.BookView.as_view(), name = 'books'),

	url(r'^create_student/$', views.create_student, name = 'create_student'),
	url(r'^create_bookcategory/$', views.create_bookcategory, name = 'create_bookcategory'),
	url(r'^create_book/$', views.create_book, name = 'create_book'),

	url(r'^edit_student/(?P<student_id>\d+)/$', views.edit_student, name='edit_student'),
	url(r'^edit_bookcategory/(?P<bookcategory_id>\d+)/$', views.edit_bookcategory, name='edit_bookcategory'),
	url(r'^edit_book/(?P<book_id>\d+)/$', views.edit_book, name='edit_book'),


	url(r'^delete_book/(?P<book_id>\d+)/$', views.delete_book, name = 'delete_book'),
	url(r'^delete_student/(?P<student_id>\d+)/$', views.delete_student, name = 'delete_student'),
	url(r'^delete_bookcategory/(?P<bookcategory_id>\d+)/$', views.delete_bookcategory, name = 'delete_bookcategory'),
	
	


)

