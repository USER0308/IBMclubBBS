#-*-coding:utf-8-*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from ..models import Member_Model,Member_Upload_Model,Sign_Model
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.files.base import ContentFile
import os
import json

from django.http import StreamingHttpResponse

@login_required(login_url="/mysite/login/")
def upload(request):
	if request.method == 'POST':
		get_email = request.user.username
		print("in upload")
		upload_file = request.FILES["file"]
		if upload_file.size < 20480000:
				#path = default_storage.save(upload_file.name,ContentFile(upload_file.read()))
				#tmp_file = os.path.join(settings.MEDIA_ROOT,path)
			print("upload file size fit")
			mem = get_object_or_404(Member_Model,email=get_email)
			Member_Upload_Model.objects.create(user=mem,file_path=upload_file)
			member = get_object_or_404(Sign_Model,email = get_email)
			cost = member.cost
			member.cost = cost + 5
			member.save()
			return redirect("/mysite/home_page/share/")
		#except:
		#	return HttpResponse("500")
