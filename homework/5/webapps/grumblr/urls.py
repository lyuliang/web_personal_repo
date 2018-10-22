from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from grumblr.views import *

urlpatterns = [
    path('', home),
    path('global/', home, name = 'global'),

    path('get_posts/', get_posts, name = 'get_posts'),
    path('get_posts/<str:time>', get_posts, name = 'get_posts'),
    path('get_profile_posts/<str:name>', get_profile_posts, name = 'get_profile_posts'),
    path('get_profile_posts/<str:name>/<str:time>', get_profile_posts, name = 'get_profile_posts'),
    path('get_follower_posts/', get_follower_posts, name = 'get_follower_posts'),
    path('get_follower_posts/<str:time>', get_follower_posts, name = 'get_follower_posts'),

    path('get_post_image/<int:id>', get_post_image, name = 'get_post_image'),
    path('add_post/', add_post, name = 'add_post'),
    path('profile/<str:name>', profile, name = 'profile'),
    path('follower/', follower, name = 'follower'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)