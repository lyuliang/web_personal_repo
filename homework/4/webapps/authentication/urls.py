from django.urls import path, re_path
from django.contrib.auth.views import LoginView, logout_then_login
from authentication import views

urlpatterns = [
    path('', views.signup),
    path('login', LoginView.as_view(template_name='authentication/login.html'),
         name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('logout', logout_then_login, name = 'logout'),
]