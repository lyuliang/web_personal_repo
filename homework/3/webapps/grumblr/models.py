from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=42)
	time = models.DateTimeField()
	# image = models.ImageField()

	def __str__(self):
		return self.text
