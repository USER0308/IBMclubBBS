#-*-coding:utf-8-*-
from django.db import models
from mysite.models import Member_Model,Post_Model
from django.utils import timezone

class Comment_Model(models.Model):
	ref_post = models.ForeignKey(Post_Model)
	floor = models.IntegerField(default=2)
	parent_floor = models.ForeignKey('self',blank=True,null=True)
	author = models.CharField(null=False,default='NoBody',max_length=20)
	content = models.CharField(null=False,max_length=10240)
	time = models.DateTimeField('发表时间',null=False,default=timezone.now)

	class Meta:
		unique_together = ("ref_post","floor")

	
