#-*-coding:utf-8-*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from mysite.models import Member_Model
import json

@login_required(login_url='/mysite/login/')
def member_info(request):
	if request.is_ajax():
		print("in member_info_ajax")
		get_author = request.POST["author_name"]
		print(get_author)
		#num = Member_Model.objects.filter(email=get_author).count()
		#if num
		obj = get_object_or_404(Member_Model,nick_name=get_author)
		print(obj.email,obj.nick_name,obj.department,obj.phone_number,obj.address)
		return HttpResponse(json.dumps({"status":"200",
										"email":obj.email,
										"nick_name":obj.nick_name,
										"department":obj.department,
										"phone_number":obj.phone_number,
										"address":obj.address}))
		
