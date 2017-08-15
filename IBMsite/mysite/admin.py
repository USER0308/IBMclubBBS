# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Application_Model,Member_Model,Post_Model
# Register your models here.
class Application_ModelAdmin(admin.ModelAdmin):
	list_display = ( 'applicant_name','apply_department' )

class Member_ModelAdmin(admin.ModelAdmin):
	list_display = ( 'email','nick_name','department' )

class Post_ModelAdmin(admin.ModelAdmin):
	list_display = ( 'theme','author','time','section' )

admin.site.register(Application_Model,Application_ModelAdmin)
admin.site.register(Member_Model,Member_ModelAdmin)
admin.site.register(Post_Model,Post_ModelAdmin)
