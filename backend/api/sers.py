from rest_framework import serializers
from . import models

class UserSer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = '__all__'