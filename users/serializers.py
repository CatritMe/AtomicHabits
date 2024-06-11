from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """сериалайзер для пользователей"""
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "tg_nick", "is_active", "password",)
        