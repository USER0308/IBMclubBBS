#-*-coding:utf-8-*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from mysite.models import Sign_Model
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.files.base import ContentFile
import os
import json
from django.http import FileResponse
from django.http import StreamingHttpResponse

@login_required(login_url="/mysite/login/")
def download(request):
	get_email = request.user.username
	mem = get_object_or_404(Sign_Model,email=get_email)
	if mem.cost >=20:
		mem.cost = mem.cost - 20
		mem.save()
	else :
		return HttpResponse(json.dumps({'data':'lack of points'}))
	file_name = request.POST["file_name"]
	full_path = os.path.join(settings.MEDIA_ROOT,file_name)
	response = HttpResponse(open(full_path,'rb'),content_type='text/html')
	response['Content-Disposition'] = 'attachment; filename="Test.java"'
	response['Content-Encoding'] = 'utf-8'
	response['Content-Location'] = "127.0.0.1:8000/media/"+file_name
	print(response)
#	response['content'] = open(full_path,'rb')
	print(response)
	return response
#	response = StreamingHttpResponse(get_obj)
#	response['Content-Type'] = 'application/octet-stream'
#	response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
#	return response

