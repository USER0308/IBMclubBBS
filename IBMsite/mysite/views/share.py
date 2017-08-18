#-*-coding:utf-8-*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from mysite.models import Member_Model,Post_Model,Comment_Model
import json

@login_required(login_url="/mysite/login/")
def share(request):
	user = request.user.username
	return render(request,'share_templates.html',{'user':user})
