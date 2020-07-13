from django.urls import path
from . import views



urlpatterns = [
    path('', views.index , name='index'),
    path('blog', views.blog, name='blog'),
    path('blog/posts/<int:post_id>', views.post, name='post'),
    path('contact', views.contact, name='contact'),
    path('gcontact', views.gcontact, name='gcontact'),
    path('gcomment', views.gcomment, name='gcomment'),
]
