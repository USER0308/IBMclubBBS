#-*-coding:utf-8-*-
from django import forms
from django.forms import fields
from mysite.models import Application_Model,Member_Model

class Application_Form(forms.ModelForm) :
#	applicant_id = Form.AutoField(primary_key=True)
	email = fields.EmailField(
		label='email',
		required=True,
		error_messages={
		'invalid':'invalid input'		
	})
	applicant_name = fields.CharField(
		label='applicant_name',
		min_length=6,
		max_length=32,
		required=True,
		error_messages={
			'required':'empty input',
			'min_length':'too short,at least 6 char',
			'max_length':'too longth, at most 32 char'
		})
	apply_department = forms.ChoiceField(label='apply_department',choices=[(u'秘书部','秘书部'),(u'人力资源部','人力资源部'),(u'宣传部','宣传部'),(u'组织部','组织部')],widget=forms.Select())
	reason = fields.CharField(label='reason',max_length=200,widget=forms.Textarea)
	class Meta:
		app_label='mysite'
		model = Application_Model
		fields = ('email','applicant_name','apply_department','reason')

	def __init__(self, *args, **kwargs):
		super(Application_Form, self).__init__(*args, **kwargs)
		# assign a (computed, I assume) default value to the choice field
		self.initial['apply_department'] = '组织部'


class Sign_Up_Form(forms.ModelForm):
	email = fields.EmailField(
		label='email',
		required=True,
		error_messages={
		'invalid':'invalid input'		
	})
	code = fields.CharField(
		label='code',
		min_length=10,
		max_length=10,
		required=True,
		error_messages={
			'required':'empty input',
			'min_length':'it should be 10 char',
			'max_length':'it should be 10 char'
		})
	password = fields.CharField(label='password',max_length=128,required=True,widget=forms.PasswordInput)
	password_confirm = fields.CharField(label='password_confirm',max_length=128,required=True,widget=forms.PasswordInput)
	
	nick_name = fields.CharField(label='nick_name',required=False,max_length=20)
	department = forms.ChoiceField(label='department',choices=[('秘书部','秘书部'),('人力资源部','人力资源部'),('宣传部','宣传部'),('组织部','组织部')])
	phone_number = fields.CharField(label='phone_number',required=False,max_length=11,min_length=11)
	address = fields.CharField(label='address',required=False,max_length=10)
	class Meta:
		app_label='mysite'
		model = Member_Model
		fields = ('email','password','nick_name','department','phone_number','address')

	def clean(self):
		#email has been used?
		get_email = self.cleaned_data['email']
		is_email_exist = Member_Model.objects.filter(email=get_email).exists()
		if is_email_exist:
			raise forms.ValidationError("this email has been used")
		# password
		password_1 = self.cleaned_data.get("password")
		password_2 = self.cleaned_data.get("password_confirm")
		if password_1 and password_2 and password_1 != password_2:
			raise forms.ValidationError(_('password confirm failed'))
		#code and password are satisfy
		get_code = self.cleaned_data.get("code")
		is_satisfy = Code.objects.filter(email=get_email,code=get_code).exists()
		if not is_satisfy:
			raise forms.ValidationError(_('code and email are not satisfy'))
		return self.cleaned_data

#	def clean_password_confirm(self):
		
#		return password_2

#	def code_satisfy(self):
#		get_email = self.cleaned_data.get("email")
#		get_code = self.cleaned_data.get("code")
#		count = Code.obects.filter(email=get_email,code=get_code).count()
#		if count == 1:
#			return True
#		else:
#			return False
