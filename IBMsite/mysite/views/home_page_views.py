from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from mysite.views import Member_Model

@login_required(login_url='/mysite/login/')
def home_page(request):
	get_email = request.user.username
	user = Member_Model.objects.get(email=get_email)
	get_costs = user.costs
	get_nick_name = user.nick_name
	get_department = user.department
	
	return render_to_response('main.html',{'email':get_email,'cost':get_costs,'nick_name':get_nick_name,'department':get_department})
