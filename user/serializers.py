import hashlib
from django.contrib.auth.models import User
from user.models import CustomUserModel
from rest_framework import serializers
# from user.models import Userlist


class ShortUserProfileSerializer(serializers.ModelSerializer):
    
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name


    class Meta:
        model = CustomUserModel
        fields = ('id', 'username', 'full_name')


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUserModel
        exclude = ('password',)



class RequestSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUserModel
        fields = ['first_name','last_name','username','email','token']

    

        

class RequestLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True, max_length=30, allow_blank=False 
    )
    password = serializers.CharField(
        required=True, max_length=128, allow_blank=False 
    )


class RequestGetSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        required=False, allow_blank=False, max_length=100)
    last_name = serializers.CharField(
        required=False, allow_blank=False, max_length=100
    )

    def validate(self, data):
        if 'first_name' not in data and 'last_name' not in data:
            raise serializers.ValidationError(
                'At least one of firstname or lastname parameters are required'
            ) 
        return data

class UserProfileEdit(serializers.Serializer):
    token = serializers.UUIDField(required = True)
    first_name = serializers.CharField(
        required=False, allow_blank=False, max_length=100)
    last_name = serializers.CharField(
        required=False, allow_blank=False, max_length=100
    )






class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']




    

        