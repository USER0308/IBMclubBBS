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
from django.core import serializers
import json

@login_required(login_url="/mysite/login/")
def get_messages(request,contacter):
    get_email = request.user.username
    print contacter
    receiver = get_object_or_404(Member_Model,email=get_email)
    sender = get_object_or_404(Member_Model,email=contacter)

    receive_messages = Chat_Model.objects.filter(msg_to=receiver,msg_from=sender)
    send_messages = Chat_Model.objects.filter(msg_to=sender, msg_from=receiver)
    for message in receive_messages:
        print message.read_status   #change it to true
    receive_messages = serializers.serialize("json", receive_messages)
    send_messages = serializers.serialize("json", send_messages)
    #print receive_messages
    #print send_messages
    return HttpResponse(json.dumps({'receive_messages':receive_messages,
                                   'send_messages':send_messages }))