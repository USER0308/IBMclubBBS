#-*-coding:utf-8-*-
from django.db import models

class Member_Model(models.Model):
	member_id = models.AutoField(primary_key=True)
	email = models.EmailField(null=False) 
	nick_name = models.CharField(null=True,max_length=20)
	department = models.CharField(null=True,max_length=12,choices=((u'秘书部','秘书部'),(u'人力资源部','人力资源部'),(u'宣传部','宣传部'),(u'组织部','组织部'),(u'主席','主席'),(u'秘书部部长','秘书部部长'),(u'人力资源部部长','人力资源部部长'),(u'宣传部部长','宣传部部长'),(u'组织部部长','组织部部长')))
	phone_number = models.CharField(null=True,max_length=11)
	address = models.CharField(null=True,max_length=10)
	class Meta:
		app_label='mysite'
		verbose_name = "Member"

	def __unicode__(self):
		return self.email
