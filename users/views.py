from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """вьюсет для модели пользователя по CRUD"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """При создании пользователя хэшировать пароль"""
        user = serializer.save(is_active=True)
        user.set_password(str(user.password))
        user.save()

    def get_permissions(self):
        """Проверка прав доступа"""
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
