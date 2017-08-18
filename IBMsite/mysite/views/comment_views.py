#-*-coding:utf-8-*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from mysite.models import Member_Model,Post_Model,Comment_Model
import json

@login_required(login_url='/mysite/login/')
def comment(request):
	get_email = request.user.username
	obj = Member_Model.objects.get(email=get_email)
	get_nick_name = obj.nick_name
	if get_nick_name is None:
		get_nick_name = get_email
	print("in comment")
	if request.is_ajax():
		print("in ajax")
		id = request.POST["id"]
		get_post= get_object_or_404(Post_Model, post_id=id)
		floor_num = get_post.comment_model_set.all().count()
		get_parent_floor = request.POST["parent_floor"]
		get_content = request.POST["content"]
		if int(get_parent_floor) == 1 :
			print("in if")
			Comment_Model.objects.create(ref_post=get_post,
										floor=int(floor_num)+2,
										author=get_nick_name,
										content=get_content)
		else :
			print("in else")
			Comment_Model.objects.create(ref_post=get_post,
										floor=int(floor_num)+2,
										parent_floor=get_object_or_404(Comment_Model,ref_post=get_post,floor=int(get_parent_floor)),
										author=get_nick_name,
										content=get_content)

		print(id+get_nick_name+get_content)
		return HttpResponse(json.dumps({"status":"200"}))
		#if not is_exists:
		#	Sign_Model.objects.create(email=get_email,cost=5,last_sign=now())
		#	return HttpResponse(json.dumps({"data":"post_success"}))
		#obj = Sign_Model.objects.get(email=get_email)
		#if obj.last_sign.date() != now().date():
		#	obj.cost = obj.cost + 5
		#	obj.last_sign = now()
		#	obj.save()
		#	return HttpResponse(json.dumps({"data":"post_success"}))
		#else:
		#	return HttpResponse(json.dumps({"data":"post_again"}))
