from django.db import models

class Manager_Model(models.Model):
	member_id = models.ForeignKey("Member_Model",null=False)
	position = models.CharField(max_length=10)
	class Meta:
		app_label='mysite'

	def __str__(self):
		return str(self.member_id)
