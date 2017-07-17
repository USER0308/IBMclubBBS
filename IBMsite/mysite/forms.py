from django import forms
from django.forms import fields
from mysite.models import Application_Model

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
	apply_department = forms.ChoiceField(label='department',choices=[('1','A'),('2','B'),('3','C'),('4','D'),('5','E')])
	reason = fields.CharField(label='reason',max_length=200,widget=forms.Textarea)
	class Meta:
		app_label='mysite'
		model = Application_Model
		fields = ('email','applicant_name','apply_department','reason')
