#This file helps to parse JSON files came from HTTP methods

from rest_framework import serializers
from .models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['name', 'surname']