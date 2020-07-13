from pages.models import Post
from rest_framework import serializers
from django.contrib.auth.models import User



class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'show_possibility' : {'read_only':True}
        }
        model = User
        fields = (  "id",
                    "is_superuser",
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "is_staff",
                    "is_active"
                    )