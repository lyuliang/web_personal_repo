from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from profiles.models import save_user_profile, create_user_profile


class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        post_save.connect(create_user_profile, sender=User)
        post_save.connect(save_user_profile, sender=User)