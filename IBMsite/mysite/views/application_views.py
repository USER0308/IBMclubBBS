from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def application(request):
    return render(request,'application_templates.html')
