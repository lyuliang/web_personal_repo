from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from grumblr.models import *

def checkSignup(request):

	#initial
	if (not 'username' in request.POST):
		return ''

	if not request.POST['username']:
		return 'Fill in username!'
	if not request.POST['password']:
		return 'Fill in password!'
	if not request.POST['confirm_password']: 
		return 'Confirm password!'
	if request.POST['confirm_password'] != request.POST['password']:
		return 'Confirm password does not match!'
	if not request.POST['first_name']: 
		return 'Fill in first name!'
	if not request.POST['last_name']: 
		return 'Fill in last name!'
	if len(User.objects.filter(username = request.POST['username'])) > 0:
		return 'Username already exists!'
	else:
		return 'ready';

def signup(request):
	context = {}
	if request.method == 'GET':
		return render(request, 'grumblr/signup.html', context)
	context['error'] = checkSignup(request)
	if context['error'] != 'ready':
		return render(request, 'grumblr/signup.html', context)

	user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
	# user.password = request.POST['password']
	user.first_name = request.POST['first_name']
	user.last_name = request.POST['last_name']
	user.save()
	
	login(request=request, user=user)
	return redirect('/global')











