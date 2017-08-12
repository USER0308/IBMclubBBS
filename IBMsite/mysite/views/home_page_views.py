#-*-coding:utf-8-*-
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from mysite.models import Member_Model,Post_Model,Sign_Model,JuncheePaginator
# from django.core.paginator import Paginator
# from django.core.paginator import PageNotAnInteger
# from django.core.paginator import EmptyPage


@login_required(login_url='/mysite/login/')
def home_page(request,type='main',page='1'):
	get_email = request.user.username
	user = Member_Model.objects.get(email=get_email)
	#get_costs = user.costs
	get_nick_name = user.nick_name
	get_department = user.department
	#show cost
	is_exist = Sign_Model.objects.filter(email=get_email).exists()
	if not is_exist:
		Sign_Model.objects.create(email=get_email,cost=5,last_sign=now())
	get_costs = Sign_Model.objects.get(email=get_email).cost
	#show post
	all_posts = Post_Model.objects.all()
	if type=='main':
		return_posts = all_posts.order_by('-time')
		for post in return_posts:
			print post.post_id,post.author,post.time,post.theme,post.section,post.content
	elif type=='scholar':
		return_posts = all_posts.filter(section=u'学术讨论区')
		for post in return_posts:
			print post.post_id,post.author,post.time,post.theme,post.section,post.content
	elif type=='department':
		return_posts = all_posts.filter(section=u'部门交流区')
		for post in return_posts:
			print post.post_id,post.author,post.time,post.theme,post.section,post.content
	elif type=='chat':
		return_posts = all_posts.filter(section=u'灌水区')
		for post in return_posts:
			print post.post_id,post.author,post.time,post.theme,post.section,post.content
	elif type=='jinghua':
		return_posts = all_posts.filter(section=u'精华区')
		for post in return_posts:
			print post.post_id,post.author,post.time,post.theme,post.section,post.content
	elif type=='share':
		return_posts = all_posts.filter(section=u'资源共享区')
		for post in return_posts:
			print post.post_id,post.author,post.time,post.theme,post.section,post.content
	print("type=="+type)
	limit = 3
	paginator = JuncheePaginator(return_posts, limit)
	try:
		return_posts = paginator.page(page)
	except PageNotAnInteger:
		return_posts = paginator.page(1)
	except EmptyPage:
		return_posts = paginator.page(paginator.num_pages)
	return render_to_response('main.html',{'email':get_email,
											'cost':get_costs,
											'nick_name':get_nick_name,
											'department':get_department,
											'posts':return_posts,
											'type':type})
