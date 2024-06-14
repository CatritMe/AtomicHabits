from datetime import datetime, timedelta, date

import pytz
from celery import shared_task

from config import settings
from habits.models import Habit
from habits.services import send_message

"""
Запуск на Windows, одновременно в разных терминалах:
1. celery -A config worker -P eventlet -l info
2. celery -A config.celery beat -l info
"""


@shared_task
def new_habit(pk):
    """Отправка уведомления при создании привычки"""
    instance = Habit.objects.filter(pk=pk).first()

    if instance.periodicity == 1:
        periodicity = 'ежедневно'
    elif 2 <= instance.periodicity <= 4:
        periodicity = f'каждые {instance.periodicity} дня'
    else:
        periodicity = f'каждые {instance.periodicity} дней'

    text = f'Вы создали новую привычку "{instance.action}", выполняется в {instance.start_time} {periodicity}'
    send_message(text, instance.user.tg_chat_id)


@shared_task
def reminder():
    """Напоминание выполнить привычку"""
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(zone).time()
    delta = ((datetime.combine(date(1, 1, 1), now) + timedelta(minutes=10)).time())

    habits = Habit.objects.all()

    for hab in habits:
        if now <= hab.start_time <= delta:
            text = (f'Напоминание выполнить привычку {hab.action}.'
                    f'Место выполнения: {hab.place},'
                    f'Время на выполнение {hab.action_time}')
            send_message(text, hab.user.tg_chat_id)
