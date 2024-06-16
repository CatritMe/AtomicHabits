from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from habits.services import notification_schedule
from habits.tasks import new_habit
from users.permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):

    """Вьюсет для модели привычки по CRUD"""

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def perform_create(self, serializer):
        """
        - при создании курса присваивать его создавшему юзеру;
        - запуск функции по отправке сообщения;
        - создание периодической задачи
        """
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()
        new_habit.delay(habit.pk)
        notification_schedule(habit.pk)

    def get_queryset(self):
        """Выбор queryset, чтобы исключить привычки других пользователей"""
        user = self.request.user
        if user.is_superuser:
            queryset = Habit.objects.all()
        else:
            queryset = Habit.objects.filter(user=user)
        return queryset

    def get_permissions(self):
        if self.action in ['create', 'list']:
            permission_classes = [IsAuthenticated | IsOwner]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]


class PublicHabitsListAPIView(ListAPIView):

    """Контроллер для списка публичных привычек"""

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = HabitPaginator
