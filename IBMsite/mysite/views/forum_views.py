from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from mysite.views import Member_Model
from mysite.forms import Change_Info_Form

@login_required(login_url='/mysite/login/')
def new_post(request):
	pass
@login_required(login_url='/mysite/login/')
def change_info(request):
	get_email = request.user.username
	get_user = Member_Model.objects.get(email=get_email)
	get_form = Change_Info_Form(initial={'nick_name':get_user.nick_name,'phone_number':get_user.phone_number,'address':get_user.address})
	return render(request,'change_info_templates.html',{'form':get_form,'email':get_email})
#	return render('change_info_templates.html')

@login_required(login_url='mysite/login/')
def save_new_info(request):
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		get_email = request.user.username
		get_user = Member_Model.objects.get(email=get_email)
		get_form = Change_Info_Form(request.POST)
		if get_form.is_valid():
			get_user.nick_name = get_form.cleaned_data['nick_name']
			get_user.phone_number = get_form.cleaned_data['phone_number']
			get_user.address = get_form.cleaned_data['address']
			get_user.save()
			return redirect('/mysite/home_page/')
		else:
			pass

def show_post_by_time(request):
	pass
def show_post_by_block(request):
	pass
