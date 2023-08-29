from rest_framework import serializers
from .models import PasswordStorage

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordStorage
        fields = ('title_storage', 'user_password', 'discription')