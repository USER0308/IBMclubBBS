#-*-coding:utf-8-*-
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from ..models import Member_Model,Chat_Model
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.files.base import ContentFile
import os
import json

@login_required(login_url="/mysite/login/")
def chat(request):
    get_email = request.user.username
    obj = get_object_or_404(Member_Model,email=get_email)
    query_set = Chat_Model.objects.filter(msg_to=obj)
    print query_set
    return render(request,"chat_templates.html",{'query_set': query_set})