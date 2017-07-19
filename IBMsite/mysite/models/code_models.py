from django.db import models

class Code_Model(models.Model):
	code = models.CharField(max_length=10,primary_key=True)
	member_id = models.ForeignKey("Manager_Model",null=False)
	email = models.EmailField(null=False)
