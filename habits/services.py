import json

import requests
from django_celery_beat.models import PeriodicTask, CrontabSchedule

from config import settings
from habits.models import Habit


def send_message(text, chat_id):
    """Отправляет сообщение в ТГ"""
    token = settings.TELEGRAM_API_KEY
    if not chat_id:
        chat_id = settings.TELEGRAM_CHAT_ID

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
       "chat_id": chat_id,
       "text": text,
    }
    resp = requests.get(url, params=params)
    print(resp.json())


def notification_schedule(habit_pk):
    """Создание периодической задачи"""
    habit = Habit.objects.get(pk=habit_pk)
    habit_time = habit.start_time
    periodicity = f'1-31/{habit.periodicity}'
    schedule, _ = CrontabSchedule.objects.get_or_create(minute=habit_time.minute, hour=habit_time.hour,
                                                        day_of_month=periodicity)
    PeriodicTask.objects.create(
        crontab=schedule,
        name=f'Notification of an action № {habit_pk}',
        task='habits.tasks.reminder',
        args=json.dumps([habit_pk])
    )
