#-*-coding:utf-8-*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from mysite.models import Member_Model,Member_Upload_Model
import json

@login_required(login_url="/mysite/login/")
def share(request):
	user = request.user.username
	objs = Member_Upload_Model.objects.all()
	return render(request,'share_templates.html',{'user':user,'upload_files':objs})
