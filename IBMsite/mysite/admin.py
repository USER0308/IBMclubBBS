# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Application_Model,Member_Model,Post_Model,Chat_Model,Member_Upload_Model,Comment_Model,Code_Model,Manager_Model
# Register your models here.
class Application_ModelAdmin(admin.ModelAdmin):
	list_display = ( 'applicant_name','apply_department' )

class Member_ModelAdmin(admin.ModelAdmin):
	list_display = ( 'email','nick_name','department' )

class Post_ModelAdmin(admin.ModelAdmin):
	list_display = ( 'theme','author','time','section' )

class Chat_ModelAdmin(admin.ModelAdmin):
	list_display = ( 'msg_from','msg_to','read_status','time' )

class Member_Upload_ModelAdmin(admin.ModelAdmin):
	list_display = ( 'user','file_path','upload_time' )

class Code_ModelAdmin(admin.ModelAdmin):
	list_display = ( 'email','code' )

class Comment_ModelAdmin(admin.ModelAdmin):
	list_display = ( 'ref_post','content','author','time' )

class Manager_ModelAdmin(admin.ModelAdmin):
	list_display = ( 'member_id','position' )

admin.site.register(Application_Model,Application_ModelAdmin)
admin.site.register(Member_Model,Member_ModelAdmin)
admin.site.register(Post_Model,Post_ModelAdmin)
admin.site.register(Chat_Model,Chat_ModelAdmin)
admin.site.register(Member_Upload_Model,Member_Upload_ModelAdmin)
admin.site.register(Code_Model,Code_ModelAdmin)
admin.site.register(Comment_Model,Comment_ModelAdmin)
admin.site.register(Manager_Model,Manager_ModelAdmin)
