from django.db import models

class Sign_Model(models.Model):
	email = models.EmailField(null=False) 
	cost = models.PositiveSmallIntegerField(null=False,default=0)
	last_sign = models.DateTimeField('time',null=False)

