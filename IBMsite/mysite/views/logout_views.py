from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout

def logout_view(request):
	logout(request)
	return HttpResponse('logout successfully')
