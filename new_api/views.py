from rest_framework import viewsets ,permissions
from pages.models import Post
from .serializers import PostSerializer ,UserSerializer
from django.contrib.auth.models import User




class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
