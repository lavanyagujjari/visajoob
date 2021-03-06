from rest_framework import serializers
from tutorial.models import UserProfileInfo

class User_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
         model = UserProfileInfo
         fields = ('username','mobileno','email','id')

class CUser_UpdateSerializer(serializers.ModelSerializer):
    class Meta:
         model = UserProfileInfo
         fields = ('is_staff','admin_status')

    def update(self, instance, validated_data): 
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.admin_status = validated_data.get('admin_status', instance.admin_status)
        instance.save()
        return instance