from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    pleasant = serializers.SerializerMethodField()

    class Meta:
        model = Habit
        fields = '__all__'

    @staticmethod
    def get_pleasant(instance):
        if instance.is_connected:
            return Habit.objects.filter(user=instance.user,
                                        is_pleasant=True,
                                        start_time__gte=instance.start_time,
                                        start_time__lte='23:59').first().action
