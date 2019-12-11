from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers,HyperlinkedModelserializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']

class GroupSerializer(serializers,HyperlinkedModelserializer):
    class Meta:
        model = Group
        fields = ['url','username']
