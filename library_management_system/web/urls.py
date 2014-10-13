from django.conf.urls  import patterns,url
from web import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'library_management_system.views.home', name='home'),
    # url(r'^library_management_system/', include('library_management_system.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
	
	url(r'^$', 'web.views.index', name='index'),

)

