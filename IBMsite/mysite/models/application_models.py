from django.db import models
#from django import forms
#from django.forms import fields

#create application model
class Application_Model(models.Model) :
	applicant_id = models.AutoField(primary_key=True)
	email = models.EmailField()
	applicant_name = models.CharField(max_length=32)
	apply_department = models.CharField(max_length=12,choices=[('1','A'),('2','B'),('3','C'),('4','D'),('5','E')])
	reason = models.TextField()
	class Meta:
		app_label='mysite'

	def __str__(self):
		return self.applicant_id

#	def submit(self):
#		self.save()
