from django.urls import path

from habits.apps import HabitsConfig
from rest_framework.routers import DefaultRouter

from habits.views import HabitViewSet, PublicHabitsListAPIView

app_name = HabitsConfig.name

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')

urlpatterns = [
    path('public_habits/', PublicHabitsListAPIView.as_view(), name='public_habits')
] + router.urls
