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
from django.db import transaction

# @login_required
# def home(request):
#
# 	# return render(request, 'global.html', {})
#
# 	context = {}
# 	context['current_user'] = request.user
# 	context['PostList'] = Post.objects.all().order_by('-time')
#
# 	if request.method == 'GET':
# 		context['form'] = PostForm()
# 		return render(request, 'grumblr/global.html', context)
#
# 	new_post = Post(user=request.user, time=datetime.datetime.now())
# 	new_post.with_image = 'image' in request.FILES.keys()
# 	form = PostForm(request.POST, request.FILES, instance=new_post)
#
# 	if not form.is_valid():
#
# 		context['form'] = form
# 		return render(request, 'grumblr/global.html', context)
#
# 	form.save()
# 	context['PostList'] = Post.objects.all().order_by('-time')
# 	context['form'] = PostForm()
# 	return render(request, 'grumblr/global.html', context)

@login_required
def home(request):
	context = {}
	print("here?\n")
	context['current_user'] = request.user
	if request.method == 'GET':
		context['form'] = PostForm()
		return render(request, 'grumblr/global.html', context)

@login_required
@transaction.atomic
def get_posts(request, time="1970-01-01T00:00+00:00"):
	max_time = Post.get_max_time()
	posts = Post.get_posts(time)
	context = {"max_time": max_time, "posts": posts}
	return render(request, 'posts.json', context, content_type='application/json')

@login_required
@transaction.atomic
def get_profile_posts(request, name, time="1970-01-01T00:00+00:00"):
	userSpecified = get_object_or_404(User, username=name)
	max_time = Post.get_profile_max_time(userSpecified)
	posts = Post.get_profile_posts(userSpecified, time)
	context = {"max_time": max_time, "posts": posts}
	return render(request, 'posts.json', context, content_type='application/json')

@login_required
@transaction.atomic
def get_follower_posts(request, time="1970-01-01T00:00+00:00"):
	print("\n get follower posts\n")
	max_time = Post.get_follower_max_time(request.user)
	posts = Post.get_follower_posts(request.user, time)
	context = {"max_time": max_time, "posts": posts}
	return render(request, 'posts.json', context, content_type='application/json')

@login_required
@transaction.atomic
def add_post(request):
	# context = {}
	# context['current_user'] = request.user
	new_post = Post(user=request.user, time=datetime.datetime.now())
	# new_post.with_image = 'image' in request.FILES.keys()
	form = PostForm(request.POST, request.FILES, instance=new_post)
	if not form.is_valid():
		raise Http404
	else:
		form.save()
	return HttpResponse("")

@login_required
def profile(request, name):
	context = {}
	userSpecified = get_object_or_404(User, username=name)
	context['specified_user'] = userSpecified.profile
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
	context['current_user'] = request.user
	return render(request, 'grumblr/follower.html', context)