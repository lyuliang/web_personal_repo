from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=42)
    time = models.DateTimeField()
    image = models.ImageField(upload_to='post_images/',
                              blank=True,
                              null=True)
    with_image = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    @staticmethod
    def get_posts(time="1970-01-01T00:00+00:00"):
        return Post.objects.filter(time__gt=time).distinct().order_by("-time")
    @staticmethod
    def get_profile_posts(user, time="1970-01-01T00:00+00:00"):
        return Post.objects.filter(user=user, time__gt=time).distinct().order_by("-time")

    @staticmethod
    def get_follower_posts(user, time="1970-01-01T00:00+00:00"):
        followers = user.profile.followers.all()
        return Post.objects.filter(user__in=followers, time__gt=time).distinct().order_by("-time")

    @property
    def html(self):
        return render_to_string('post_template.html', {
            # 'id': self.id,
            # 'text': self.text,
            # 'time': self.time,
            # 'username': self.user.username,
            'Post': self,
        }).replace('\n', '')

    @staticmethod
    def get_max_time():
        return Post.objects.all().aggregate(Max('time'))['time__max'] or "1970-01-01T00:00+00:00"

    @staticmethod
    def get_profile_max_time(user):
        return Post.objects.filter(user=user).aggregate(Max('time'))['time__max'] or "1970-01-01T00:00+00:00"

    @staticmethod
    def get_follower_max_time(user):
        followers = user.profile.followers.all()
        return Post.objects.filter(user__in=followers).aggregate(Max('time'))['time__max'] or "1970-01-01T00:00+00:00"

class Comment(models.Model):
    text = models.CharField(max_length=42)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    # Returns all recent additions to the to-do list.
    @staticmethod
    def get_comments(post_id):
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post).distinct().order_by("time")
        return comments

    # Generates the HTML-representation of a single to-do list item.
    @property
    def html(self):
        return render_to_string('comment_template.html',
                                {'Comment': self,
                                 }).replace("\n", "")



