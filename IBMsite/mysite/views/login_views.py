#-*-coding:utf-8-*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from mysite.forms import Login_Form
from django.contrib.auth import authenticate, login

def login_view(request):
	if request.method == 'GET':
		login_form = Login_Form()
		return render(request,'login_templates.html',{'form':login_form})
	elif request.method == 'POST':
		getForm = Login_Form(request.POST)
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
#			member=getForm.save(commit=False)
#			print('after save(commit)')
#			is_satisfy = getForm.code_satisfy()
#			print(is_satisfy)
#			if is_satisfy:
#				print("before save()")
#			member.save()
#				print("before save(commit)")
			get_email = getForm.cleaned_data['email']
			get_password = getForm.cleaned_data['password']
			user = authenticate(username=get_email, password=get_password)
			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('/mysite/home_page/')#should redirect to loginsuccessfully page
				else:
					print('disable account')
			else:
				print('invalid login')
#			get_email = getForm.cleaned_data['email']
#			request.session['email'] = get_email
			
#			else:
				# code and email are not the same,redirect to 
#				pass
		else:
			return render(request,'login_templates.html',{'form':getForm})
#form is not valid
#			print(getForm.errors)
			
	return render(request,'login_templates.html')
