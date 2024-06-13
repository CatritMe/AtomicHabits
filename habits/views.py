from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = (IsOwner, )
    pagination_class = HabitPaginator

    def perform_create(self, serializer):
        """при создании курса присваивать его создавшему юзеру"""
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            queryset = Habit.objects.all()
        else:
            queryset = Habit.objects.filter(user=user)
        return queryset


class PublicHabitsListAPIView(ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = HabitPaginator
