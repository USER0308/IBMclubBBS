from django.db import models

#create application model
class Application(models.Model) :
	applicant_id = models.AutoField(primary_key=True)
	email = models.EmailField()
	applicant_name = models.CharField(max_length=32)
	apply_department = models.CharField(max_length=20)
	reason = models.CharField(max_length=200)
	class Meta:
		app_label='mysite'
