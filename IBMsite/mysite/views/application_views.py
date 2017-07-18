#-*-coding:utf-8-*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from mysite.models import Application_Model
from mysite.forms import Application_Form
# Create your views here.
def application(request):
	if request.method == 'GET':
		application_form = Application_Form(initial={'apply_department':'组织部'})
		return render(request,'application_templates.html',{'form':application_form})
	elif request.method =='POST':
		getForm = Application_Form(request.POST)
#		print(request.POST['email'])
#		print(request.POST['applicant_name'])
#		print(request.POST['apply_department'])
#		print(request.POST['reason'])
#		print('before is_valid')
		v = getForm.is_valid()
#		print('after is_valid')
#		print(v)
		if v:
			print(getForm.cleaned_data)
#			application.save()
#			application.submit()
			form=getForm.save(commit=False)
			form.save()
			return redirect('/mysite/application_submit/')
		else:
			print(getForm.errors)
			return render(request,'application_templates.html',{'form':getForm})
	return render(request,'application_templates.html')

def application_submit(request):
#	if request.method == 'GET'
	return HttpResponse("Submit successfully, please wait for response")
#def save():
#class Application_Form(forms.Form) :
#	applicant_id = Form.AutoField(primary_key=True)
#	email = fields.EmailField(
#		label='email',
#		required=True,
#		error_messages={
#		'invalid':'invalid input'		
#	})
#	applicant_name = fields.CharField(
#		label='applicant_name',
#		min_length=6,
#		max_length=32,
#		required=True,
#		error_messages={
#			'required':'empty input',
#			'min_length':'too short,at least 6 char',
#			'max_length':'too longth, at most 32 char'
#		})
#	apply_department = forms.ChoiceField(label='department',choices=[(1,'A'),(2,'B'),(3,'C'),(4,'D'),(5,'E')])
#	reason = fields.CharField(label='reason',max_length=200)
#	class Meta:
#		app_label='mysite'
