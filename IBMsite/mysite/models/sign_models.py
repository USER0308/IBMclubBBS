from django.db import models

class Sign_Model(models.Model):
	cost = models.PositiveSmallIntegerField(null=False,default=0)
最后签到日期
积分
用户

状态为签到,如果当前日期不是最后签到日期,则积分增加,把最后签到日期改为今日日期,将状态改为已签到
否则提示已经签到过了


