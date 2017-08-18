#-*-coding:utf-8-*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from mysite.models import Member_Model,Post_Model,Comment_Model
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.files.base import ContentFile
import os
import json

def upload(request):
	if request.method == 'POST':
		get_email = request.user.username
		print("in upload")
		try:
			upload_file = request.FILES["file"]
			if upload_file.size > 1000 and upload_file.size < 204800:
				path = default_storage.save(upload_file.name,ContentFile(upload_file.read()))
				tmp_file = os.path.join(settings.MEDIA_ROOT,path)
				return HttpResponse("200")
		except:
			return HttpResponse("500")
