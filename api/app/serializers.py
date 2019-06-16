# from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Contact

# class ArticleSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Article
#         fields = ("id", "title", "category", "date", "text", "image")

# class NewsSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = News
#         fields = ("id", "title", "category", "date", "text", "image")

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=False)

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'profile', 'password')

#     def create(self, validated_data):
#         return User.objects.create_user(request_data=validated_data)

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ("name", "email", "tell", "text", "title")