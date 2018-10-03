from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from profiles.views import *
from grumblr.views import *

urlpatterns = [
    path('', home),
    path('get_profile_image/<str:name>', get_profile_image, name = 'get_profile_image'),
    path('edit/', edit, name = 'edit'),
    path('add_follower/<str:name>', add_follower, name = 'add_follower'),
    path('remove_follower/<str:name>', remove_follower, name = 'remove_follower')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)