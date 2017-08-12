from django.shortcuts import render, get_object_or_404
from django.http.HttpResponse import HttpResponse
from mysite.models import Post_Model

def post_detail(request, num):
	post = get_object_or_404(Post_Model, post_id=num)
    #return render(request, 'blog/post_detail.html', {'post': post})
	return HttpResponse("good")
