from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Queue, QueueSpecial


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class QueueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Queue
        fields = ['url', 'numero', 'atendente', 'guiche',  'buzz', 'created_at', 'updated_at']

class QueueSpecialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QueueSpecial
        fields = ['url', 'numero', 'atendente', 'guiche', 'buzz', 'created_at', 'updated_at']
