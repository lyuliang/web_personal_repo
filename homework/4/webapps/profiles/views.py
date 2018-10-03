from django.shortcuts import render, redirect, reverse
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from mimetypes import guess_type
from profiles.models import *
from profiles.forms import *
from grumblr.models import *

@login_required
def edit(request):
	context = {}
	context['current_user'] = request.user

	my_profile = Profile.objects.get(user=request.user)
	if request.method == 'GET':
		context['form'] = ProfileForm(instance=my_profile)

		return render(request, 'profiles/edit.html', context)
	form = ProfileForm(request.POST, request.FILES, instance=my_profile)
	if not form.is_valid():
		context['form'] = form
		return render(request, 'profiles/edit.html', context)

	form.save()

	context['form'] = ProfileForm(instance=my_profile)
	return render(request, 'profiles/edit.html', context)

@login_required
def get_profile_image(request, name):
	profile = Profile.objects.get(user=User.objects.get(username=name))
	if not profile.image:
		raise Http404
	content_type = guess_type(profile.image.name)
	return HttpResponse(profile.image, content_type =content_type)

@login_required
def add_follower(request, name):
	context = {}
	user_to_follow = User.objects.get(username=name)
	if user_to_follow not in request.user.profile.followers.all():
		request.user.profile.followers.add(user_to_follow)
		context['result'] = 'Successfully followed!'
	else:
		context['result'] = 'Already followed'
	userSpecified = User.objects.get(username__exact=name)
	context['PostList'] = Post.objects.filter(user=userSpecified).order_by('-time')
	context['specified_user'] = userSpecified.profile
	context['specified_username'] = userSpecified.username
	context['current_username'] = request.user.username
	return render(request, 'grumblr/profile.html', context)

@login_required
def remove_follower(request, name):
	context = {}
	user_to_remove = User.objects.get(username=name)
	if user_to_remove in request.user.profile.followers.all():
		request.user.profile.followers.remove(user_to_remove)
		context['result'] = 'Successfully unfollowed!'
	else:
		context['result'] = 'Already unfollowed'
	userSpecified = User.objects.get(username__exact=name)
	context['PostList'] = Post.objects.filter(user=userSpecified).order_by('-time')
	context['specified_user'] = userSpecified.profile
	context['specified_username'] = userSpecified.username
	context['current_username'] = request.user.username
	return render(request, 'grumblr/profile.html', context)