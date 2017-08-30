#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from mysite.models import Member_Model,Code_Model,Manager_Model
import json
import random
import string

@login_required(login_url='/admin/')
def send_email(request):
	print("in send_email")
	get_email = request.user.username
	print request.body
	#obj = Member_Model.objects.get(email=get_email)

	def _format_addr(s):
		name, addr = parseaddr(s)
		return formataddr(( \
			Header(name, 'utf-8').encode(), \
			addr.encode('utf-8') if isinstance(addr, unicode) else addr))

	from_addr = '1341262679@qq.com'
	password = 'gtutlwpegvvmigeb'
	to_addr = request.POST["email_addr"]
	print to_addr
	smtp_server = 'smtp.qq.com'
	smtp_port = 587

	print "finding administrator"
	manager = get_object_or_404(Manager_Model,position="admin")
	print "finishing finding"
	if manager==None:
		print("manager not found")
	print "finding administratir finish,finding code_obj"
	invite = string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 10)).replace(' ','')
	print invite
	code_obj = Code_Model.objects.create( member_id=manager,code=invite,email=to_addr)
	print "finding obj"
	if code_obj==None:
		print("code_obj not found")

	print("code_obj is ")
	print code_obj
	msg = MIMEText(u'你好,你的邀请码为'+invite, 'plain', 'utf-8')
	msg['From'] = _format_addr(u'管理员 <%s>' % from_addr)
	msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
	msg['Subject'] = Header(u'来自华南理工大学IBM主机创新俱乐部的问候 ^_^!', 'utf-8').encode()
	print msg
	try:
		server = smtplib.SMTP(smtp_server, smtp_port)
		server.starttls()
		server.set_debuglevel(1)
		server.login(from_addr, password)
		server.sendmail(from_addr, [to_addr], msg.as_string())
		server.quit()
		print("done")
		Code_Model.objects.create(code="tobemember")
		return HttpResponse(json.dumps({"status":"200"}))
	except Exception, e:
		return HttpResponse(json.dumps({"status":"500"}))
		raise
	finally:
		pass
	# server = smtplib.SMTP(smtp_server, smtp_port)
	# server.starttls()
	# server.set_debuglevel(1)
	# server.login(from_addr, password)
	# server.sendmail(from_addr, [to_addr], msg.as_string())
	# server.quit()
	# print("done")
	# return HttpResponse(json.dumps({"status":"200"}))
