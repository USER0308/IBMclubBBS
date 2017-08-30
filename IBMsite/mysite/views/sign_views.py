#-*-coding:utf-8-*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from mysite.models import Sign_Model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='/mysite/login/')
@csrf_exempt
def sign(request):
	get_email = request.user.username
	print("in sign")
	if request.is_ajax():
		print("in ajax")
		is_exists = Sign_Model.objects.filter(email=get_email).exists()
		if not is_exists:
			Sign_Model.objects.create(email=get_email,cost=5,last_sign=now)
			return HttpResponse(json.dumps({"data":"post_success"}))
		obj = Sign_Model.objects.get(email=get_email)
		if obj.last_sign.date() != now().date():
			obj.cost = obj.cost + 5
			obj.last_sign = now()
			obj.save()
			return HttpResponse(json.dumps({"data":"post_success"}))
		else:
			return HttpResponse(json.dumps({"data":"post_again"}))
	#return redirect(request,'../home_page/')
	
