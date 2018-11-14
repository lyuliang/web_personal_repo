from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, default=' ')
    last_name = models.CharField(max_length=200, default=' ')
    age = models.IntegerField(null=True, blank=True)
    bio = models.CharField(max_length=420, null=True, blank=True)
    image = models.ImageField(upload_to='profile_images/',
                              default='Default.jpg',
                              null=True,
                              blank=True)
    followers = models.ManyToManyField(User,
                                       related_name='another',
                                       blank=True)


