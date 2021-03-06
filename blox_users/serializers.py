from rest_framework import serializers
from django.contrib.auth.models import User, Group


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
