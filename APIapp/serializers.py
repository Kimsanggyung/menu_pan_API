from dataclasses import field
from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = ('id', 'image', 'name', 'info', 'facts', 'price', 'allergy', 'release_date', 'update_at')