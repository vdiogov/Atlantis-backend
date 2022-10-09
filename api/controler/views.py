from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, QueueSerializer, QueueSpecialSerializer

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
 
from .models import Queue, QueueSpecial
from rest_framework.decorators import api_view, permission_classes


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username']
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class QueueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows queue to be viewed, edited or deleted.
    """
    queryset = Queue.objects.all().order_by('-created_at')
    serializer_class = QueueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class QueueBulkDelete(viewsets.ViewSet):

    def get_permissions(self):
        permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        pass

    def destroy(self, request, *args, **kwargs):
        query = Queue.objects.all().delete()
        query.save()
        return Response(data='delete success')

class QueueSpecialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows queue to be viewed, edited or deleted.
    """
    queryset = QueueSpecial.objects.all().order_by('-created_at')
    serializer_class = QueueSpecialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class QueueSpecialBulkDelete(viewsets.ViewSet):

    def get_permissions(self):
        permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        pass

    def destroy(self, request, *args, **kwargs):
        query = QueueSpecial.objects.all().delete()
        query.save()
        return Response(data='delete success')

