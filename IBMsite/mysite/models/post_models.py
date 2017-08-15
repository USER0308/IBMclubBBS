#-*-coding:utf-8-*-
from django.db import models
from mysite.models import Member_Model
from django.utils import timezone
#from ckeditor.fields import RichTextField

class Post_Model(models.Model):
	post_id = models.AutoField(null=False,primary_key=True)
	author = models.CharField(null=False,default='NoBody',max_length=20)
	time = models.DateTimeField('发表时间',null=False,default=timezone.now)
	theme = models.CharField(max_length=128)
	section = models.CharField(null=False,max_length=12,choices=[(u'学术讨论区','学术讨论区'),
																(u'部门交流区','部门交流区'),
																(u'灌水区','灌水区'),
																(u'精华区','精华区'),
																(u'资源共享区','资源共享区')])
	content = models.CharField(null=False,max_length=10240)

	class Meta:
		app_label='mysite'
		verbose_name = "post"

	def __unicode__(self):
		return self.theme
