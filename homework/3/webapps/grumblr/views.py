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

def checkLogin(request):
	if not 'username' in request.POST:
	   # and not 'password' in request.POST:
		return ''
	if not request.POST['username']:
		return 'Fill in username!'
	if not request.POST['password']:
		return 'Fill in password'
	else:
		return 'ready'

def log(request):
	if request.path == '/':
		return redirect('/login')
	context = {}
	context['error'] = checkLogin(request)
	if context['error'] != 'ready':
		return render(request, 'grumblr/login.html', context)

	user = authenticate(username=request.POST['username'], password=request.POST['password'])

	if user is not None:
		login(request=request, user=user)
		return redirect('/global')
	else:
		context['error'] = 'Invalid username or password!'
		return render(request, 'grumblr/login.html', context)

@login_required
def home(request):
	context = {}
	user = request.user

	if 'post_box' in request.POST:
		if request.POST['post_box']:

		 	new_post = Post(text=request.POST['post_box'])
		 	new_post.user = user	 	
		 	new_post.time = datetime.datetime.now()
		 	new_post.save()
		 	context['error'] = ''

	context['current_user'] = user
	context['PostList'] = Post.objects.all().order_by('-time')

	return render(request, 'grumblr/global.html', context)

@login_required
def profile(request, name):
	context = {}
	userSpecified = User.objects.get(username__exact=name)
	context['PostList'] = Post.objects.filter(user=userSpecified).order_by('-time')
	context['specified_user'] = userSpecified
	context['current_username'] = request.user.username
	return render(request, 'grumblr/profile.html', context)

def log_out(request):
	context = {}
	logout(request=request)
	return render(request, 'grumblr/login.html', context)







