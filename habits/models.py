from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Модель привычки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место')
    start_time = models.TimeField(verbose_name='время старта')
    action = models.CharField(max_length=300, verbose_name='действие')
    is_pleasant = models.BooleanField(verbose_name='приятная привычка')
    connected_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="связанная привычка", **NULLABLE)
    periodicity = models.SmallIntegerField(default=1, verbose_name='периодичность')
    prize = models.CharField(max_length=300, verbose_name='вознаграждение', **NULLABLE)
    action_time = models.DurationField(default=None, verbose_name='время выполнения', **NULLABLE)
    is_public = models.BooleanField(verbose_name='публичная привычка')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('start_time',)
