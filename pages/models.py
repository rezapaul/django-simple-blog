from django.db import models
from datetime import datetime
from django.contrib.auth.models import User




class Post(models.Model):
    auther = models.ForeignKey(User ,on_delete=models.DO_NOTHING,default=1)
    subhead = models.CharField(max_length=200)
    fullhead = models.CharField(max_length=400)
    text = models.TextField()
    point = models.TextField()
    image = models.ImageField(upload_to='post_images')
    date = models.DateTimeField(default=datetime.now , blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.subhead




class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name