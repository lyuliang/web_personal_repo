from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from mimetypes import guess_type
from grumblr.models import *
from grumblr.forms import *

@login_required
def home(request):
	context = {}
	context['current_user'] = request.user
	context['PostList'] = Post.objects.all().order_by('-time')

	if request.method == 'GET':
		context['form'] = PostForm()
		return render(request, 'grumblr/global.html', context)

	new_post = Post(user=request.user, time=datetime.datetime.now())
	form = PostForm(request.POST, request.FILES, instance=new_post)

	if not form.is_valid():

		context['form'] = form
		print('not valid')
		print(form)
		print(new_post.time)
		return render(request, 'grumblr/global.html', context)

	form.save()
	context['PostList'] = Post.objects.all().order_by('-time')
	print('valid')
	context['form'] = PostForm()
	return render(request, 'grumblr/global.html', context)

@login_required
def profile(request, name):
	context = {}
	userSpecified = User.objects.get(username__exact=name)
	context['PostList'] = Post.objects.filter(user=userSpecified).order_by('-time')
	context['specified_user'] = userSpecified.profile
	print(context['specified_user'].first_name+'lalala')
	context['specified_username'] = userSpecified.username
	context['current_username'] = request.user.username
	return render(request, 'grumblr/profile.html', context)

@login_required
def get_post_image(request, id):
	post = get_object_or_404(Post, id = id)
	if not post.image:
		raise Http404
	content_type = guess_type(post.image.name)
	return HttpResponse(post.image, content_type =content_type)

@login_required
def follower(request):
	context = {}
	followers = request.user.profile.followers.all()
	context['followers'] = followers

	context['PostList'] = Post.objects.filter(user__in= followers).order_by('-time')
	print(context['PostList'])
	return render(request, 'grumblr/follower.html', context)