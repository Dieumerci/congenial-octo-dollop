from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from cognizance.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'description']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {"write_only": True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        for user in User.objects.all():
            Token.objects.create(user=user)
        return user