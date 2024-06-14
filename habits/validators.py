from datetime import timedelta

from rest_framework.exceptions import ValidationError


class PrizeValidator:
    """Исключить одновременный выбор связанной привычки и указания вознаграждения"""

    def __init__(self, connect, prize):
        self.connect = connect
        self.prize = prize

    def __call__(self, value):
        tmp_conn = dict(value).get(self.connect)
        tmp_prize = dict(value).get(self.prize)
        if tmp_conn and tmp_prize:
            raise ValidationError('Одновременный выбор связанной привычки и указание вознаграждения невозможен')


class ActionTimeValidator:
    """Время выполнения должно быть не больше 120 секунд"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_field = dict(value).get(self.field)
        if tmp_field > timedelta(seconds=120):
            raise ValidationError('Время выполнения должно быть не более 120 секунд')


class ConnectedHabitsValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_field = value.get(self.field)
        if tmp_field:
            if not tmp_field.is_pleasant:
                raise ValidationError('В связанные привычки могут попадать только приятные привычки')


class PleasantHabitsValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки"""

    def __init__(self, is_pleasant, connect, prize):
        self.is_pleasant = is_pleasant
        self.connect = connect
        self.prize = prize

    def __call__(self, value):
        is_pleasant = dict(value).get(self.is_pleasant)
        connect = dict(value).get(self.connect)
        prize = dict(value).get(self.prize)
        if is_pleasant:
            if connect or prize:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class PeriodicityValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_field = dict(value).get(self.field)
        if tmp_field > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
