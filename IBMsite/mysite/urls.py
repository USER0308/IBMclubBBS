from django.conf.urls import url
from django.contrib import admin
from views import application,application_submit

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
	url(r'^application/$',application),#write the application, and 
	url(r'^application_submit/$',application_submit),
]
