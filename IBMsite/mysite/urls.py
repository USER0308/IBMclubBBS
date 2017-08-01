from django.conf.urls import url
from django.contrib import admin
from views import application,application_submit
from views import sign_up,home_page,login_view,logout_view,change_info,save_new_info,new_post

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
	url(r'^application/$',application),#write the application, and 
	url(r'^application_submit/$',application_submit),
	url(r'^login/$',login_view),
	url(r'^logout/$',logout_view),
	url(r'^sign_up/$',sign_up),
	url(r'^home_page/$',home_page),
	url(r'^change_info/$',change_info),
	url(r'^save_new_info/$',save_new_info),
	url(r'^new_post/$',new_post),
]
