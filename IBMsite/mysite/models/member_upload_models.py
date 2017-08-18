from django.db import models
from mysite.models import Member_Model
from django.utils import timezone

class Member_Upload_Model(models.Model):
	user = models.ForeignKey(Member_Model)
	file_path = models.FileField(upload_to = './upload/')
	upload_time = models.DateTimeField(null=False,default=timezone.now)
