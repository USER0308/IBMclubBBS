from django.conf.urls import url
from django.contrib import admin
from views import application,application_submit
from views import sign_up,home_page
urlpatterns = [
#    url(r'^admin/', admin.site.urls),
	url(r'^application/$',application),#write the application, and 
	url(r'^application_submit/$',application_submit),
#	url(r'^login/$',login),
	url(r'^sign_up/$',sign_up),
	url(r'^home_page/$',home_page),
]
