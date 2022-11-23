from dataclasses import field
from rest_framework import serializers
from .models import Menu
from django.contrib.auth.models import User

class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = ('id', 'image', 'name', 'info', 'facts', 'price', 'allergy', 'kategorie', 'release_date', 'update_at')

class UserSerializer(serializers.ModelSerializer):
  class Meta:
      model = User
      fields = ['id', 'username']