from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from mysite.models import Post_Model

def post_detail(request, num):
	post = get_object_or_404(Post_Model, post_id=num)
	comments = post.comment_model_set.all()
	print(comments.count())
	return render(request, 'post_detail.html', {'post': post,'comments':comments,'comment_range':range(1,10)})
	#return HttpResponse(str(post.post_id)+post.author)
