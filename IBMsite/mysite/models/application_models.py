#-*-coding:utf-8-*-
from django.db import models
#from django import forms
#from django.forms import fields

#create application model
class Application_Model(models.Model) :
	applicant_id = models.AutoField(null=False,primary_key=True)
	email = models.EmailField(null=False)
	applicant_name = models.CharField(null=False,max_length=32)
	apply_department = models.CharField(null=False,max_length=12,choices=[(u'秘书部','秘书部'),(u'人力资源部','人力资源部'),(u'宣传部','宣传部'),(u'组织部','组织部')],default='组织部')
	reason = models.TextField(null=False)
	class Meta:
		app_label='mysite'

	def __str__(self):
		return str(self.applicant_id)

#	def submit(self):
#		self.save()
