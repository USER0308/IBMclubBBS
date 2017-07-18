from django.db import models

class Member_Model(models.Model):
	member_id = models.AutoField(primary_key=True)
	email = models.ForeignKey("Application_Model",null=False) 
	password = models.CharField(null=False,max_length=128)
	costs = models.PositiveSmallIntegerField(null=False,default=0)
	nick_name = models.CharField(null=True,max_length=20)
	department = models.CharField(null=True,max_length=15)
	phone_number = models.CharField(null=True,max_length=11)
	address = models.CharField(null=True,max_length=10)
	class Meta:
		app_label='mysite'

	def __str__(self):
		return str(self.member_id)
