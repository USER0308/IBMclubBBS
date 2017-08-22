from django.db import models
from django.utils import timezone
from mysite.models import Member_Model

class Chat_Model(models.Model):
    msg_from = models.ForeignKey(Member_Model,related_name='from_member')
    msg_to = models.ForeignKey(Member_Model,related_name='to_member')
    time = models.DateTimeField( null=False,default=timezone.now() )
    read_status = models.BooleanField(null=False,default=False)
    content = models.CharField(null=False,max_length=10240)