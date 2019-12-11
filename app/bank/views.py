from django.contrib.auth.models import User,  Group
from rest_framework import viewsets
from .serializer import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows you to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    class_serializer = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows you to be viewed or edited.
    """
    queryset = Group.objects.all()
    class_serializer = GroupSerializer


