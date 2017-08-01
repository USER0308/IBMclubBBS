#-*-coding:utf-8-*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from mysite.forms import Login_Form
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from mysite.forms import New_Post_Form
from mysite.models import Member_Model

@login_required(login_url='/mysite/login/')
def new_post(request):
	if request.method == 'GET':
		print('method is get')
		new_form = New_Post_Form()
		return render(request,'new_post_templates.html',{'form':new_form})
	elif request.method == 'POST':
		get_form = New_Post_Form(request.POST)
#		print("check if is valid")
		v = get_form.is_valid()
#		print(v)
		if v:
			get_post = get_form.save(commit=False)
			get_email = request.user.username
			user = Member_Model.objects.get(email=get_email)
			print(get_email)
			print(user.member_id)
			get_post.author = user.nick_name
			if get_post.author is None:
				get_post.author = user.email
			get_post.save()
			return redirect('../home_page/')
	else:
		return render(request,'new_post_templates.html')
	
