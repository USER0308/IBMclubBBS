#-*-coding:utf-8-*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from mysite.models import Member_Model
from mysite.forms import Sign_Up_Form

def sign_up(request):
	if request.method == 'GET':
		sign_up_form = Sign_Up_Form(initial={'department':'组织部'})
		return render(request,'sign_up_templates.html',{'form':sign_up_form})
	elif request.method == 'POST':
		getForm = Sign_Up_Form(request.POST)
#		print("check if is valid")
		v = getForm.is_valid()
#		print(v)
		if v:
#			signup_info = getForm.cleaned_data
#			print(getForm.cleaned_data)
#			application.save()
#			application.submit()
			#confirm if the code and email is the same as 
#			print("before save(commit)")
#			department=getForm.cleaned_data['apply_department']
			member=getForm.save(commit=False)
#			print('after save(commit)')
#			is_satisfy = getForm.code_satisfy()
#			print(is_satisfy)
#			if is_satisfy:
#				print("before save()")
			member.save()
#				print("before save(commit)")
			return redirect('/mysite/home_page/')#should redirect to loginsuccessfully page
#			else:
				# code and email are not the same,redirect to 
#				pass
		else:
			return render(request,'sign_up_templates.html',{'form':getForm})
#form is not valid
#			print(getForm.errors)
			
	return render(request,'sign_up_templates.html')

def home_page(request):
#	if request.method == 'GET'
	return HttpResponse("This is home_page")
