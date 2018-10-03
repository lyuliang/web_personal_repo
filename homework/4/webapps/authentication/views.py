from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from grumblr.models import *
from authentication.forms import *
from grumblr.views import *
from profiles.models import *
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

@transaction.atomic
def signup(request):
    context = {}

    if request.method == 'GET':
        context['form'] = SignupForm()
        return render(request, 'authentication/signup.html', context)

    form = SignupForm(request.POST)
    for i in form.errors:
        print(i)
    print('xxx')
    for j in form.visible_fields():
        print(j.errors)
    context['form'] = form

    if not form.is_valid():
        return render(request, 'authentication/signup.html', context)

    # If we get here the form data was valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'],
                                        email= form.cleaned_data['email'])
    first_name = form.cleaned_data['first_name']
    last_name = form.cleaned_data['last_name']
    new_user.is_active = False
    token = default_token_generator.make_token(new_user)
    email_body = """
    Welcome to Grumblr. Please click the link below
    to Verify your email address and complete the
    registration of your account:
    http://%s%s
    """ % (request.get_host(),
           reverse('verify', args=(new_user.username, token, first_name, last_name)))
    send_mail(subject="Verify your email address for Grumblr",
              message=email_body,
              from_email="lyulianl@andrew.cmu.edu",
              recipient_list=[new_user.email])
    context['email'] = form.cleaned_data['email']
    return render(request, 'authentication/need_confirmation.html', context)


def verify(request, username, token, first_name, last_name):
    new_user = User.objects.get(username=username)
    if new_user:
        print('new_user')
        if default_token_generator.check_token(new_user, token):
            print('ok')
            new_user.is_active = True
            new_profile = Profile.objects.create(user=new_user)
            new_profile.first_name = first_name
            new_profile.last_name = last_name
            new_profile.save()
            return redirect(reverse('login'))
    print('not ok')
    return redirect(reverse('signup'))


