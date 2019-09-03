from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Comment
from .forms import CommentForm
import datetime
import pytz

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('HTTP_USER_AGENT')
    return ip

def index(request):
	comments__ = Comment.objects.all()
	comments = list(reversed(comments__))
	context = {'comments': comments,}
	return render(request, 'comments/comments.html', context)

def add(request):
	local_time = datetime.datetime.now(tz=pytz.timezone('Europe/Moscow'))

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment_instance = request.POST.get('comment', '')
			comment = Comment(commentor = get_client_ip(request), comment = comment_instance, time = str(local_time)[10:19])
			comment.save()

			comments__ = Comment.objects.all()
			comments = list(reversed(comments__))
			context = {'comments': comments,}
			return render(request, 'comments/comments.html', context)

	return render(request, 'comments/error.html')
