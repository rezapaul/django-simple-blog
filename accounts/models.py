from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    bio = models.TextField()
    photo = models.ImageField(upload_to='users_photo')

    def __str__(self):
        return self.bio



class Comment(models.Model):
    post_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    user_photo = models.CharField(max_length=300,default="http://127.0.0.1:8000/media/users_photo/author.png")
    name = models.CharField(max_length=300)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now ,blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
