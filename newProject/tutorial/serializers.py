from rest_framework import serializers
from tutorial.models import rest_form

class UserSerializer(serializers.ModelSerializer):
    class Meta:
         model = rest_form
         fields = ('name','mobile','area')