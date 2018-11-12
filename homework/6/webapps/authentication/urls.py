from django.urls import path, re_path
from django.contrib.auth.views import LoginView, logout_then_login
from authentication import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.signup),
    path('login', LoginView.as_view(template_name='authentication/login.html'),
         name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('logout', logout_then_login, name = 'logout'),
    path('verify/<str:username>/<str:token>/<str:first_name>/<str:last_name>', views.verify, name = 'verify'),

    re_path(r'^accounts/password_reset/$',
            auth_views.PasswordResetView.as_view(template_name='authentication/password_reset_form.html'),
            name="password_reset"),
    re_path(r'^accounts/password_reset/done/$',
            auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'),
            name="password_reset_done"),
    re_path(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$',
            auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'),
            name = 'password_reset_confirm'),
    re_path(r'^accounts/reset/done/$',
            auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'),
            name="password_reset_complete"),
]