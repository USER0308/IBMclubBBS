from django.db import models

class Code(models.Model):
	code = models.CharField(max_length=10,primary_key=True)
	member_id = models.ForeignKey("Manager_Model",null=False)
	email = models.ForeignKey("Application_Model",null=False)
