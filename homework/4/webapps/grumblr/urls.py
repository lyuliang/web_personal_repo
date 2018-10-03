from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from grumblr.views import *

urlpatterns = [
    path('', home),
    path('global/', home, name = 'global'),
    path('get_post_image/<int:id>', get_post_image, name = 'get_post_image'),
    path('profile/<str:name>', profile, name = 'profile'),
    path('follower/', follower, name = 'follower'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)