from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User

"""
{'ok': True,
'result': {'message_id': 4, 
            'from': {'id': 6936104865, 'is_bot': True, 'first_name': 'KateNewBot', 'username': 'Kate_new_first_bot'}, 
            'chat': {'id': 1164494619, 'first_name': 'Екатерина', 'username': 'catritme', 'type': 'private'}, 
            'date': 1718357315, 
            'text': 'Вы создали новую привычку ходить пешком час в 20:00:00'
            }
}
"""


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@ad.com', password='admin')
        self.habit = Habit.objects.create(
            user=self.user,
            place='place',
            start_time="17:27:00",
            action='action',
            is_pleasant=True,
            periodicity=2,
            action_time='00:02:00',
            is_public=True

        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse('habits:habits-detail', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('action'), 'action'
        )

    def test_habit_create(self):
        url = reverse('habits:habits-list')
        data = {
                "place": "улица",
                "start_time": "17:27:00",
                "action": "ходить пешком час",
                "is_pleasant": True,
                "periodicity": 1,
                "action_time": 120,
                "is_public": True
            }
        data1 = {
                "place": "улица",
                "start_time": "17:27:00",
                "action": "ходить пешком час",
                "is_pleasant": True,
                "periodicity": 1,
                "action_time": 150,
                "is_public": True
            }
        response = self.client.post(url, data)
        response1 = self.client.post(url, data1)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(), 2
        )
        self.assertEqual(
            response1.status_code, status.HTTP_400_BAD_REQUEST
        )

    def test_habit_update(self):
        url = reverse('habits:habits-detail', args=(self.habit.pk,))
        data = {
                "place": "улица Сезам",
                "start_time": "17:27:00",
                "action": "есть печенье",
                "is_pleasant": True,
                "periodicity": 1,
                "action_time": 60,
                "is_public": True
            }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('place'), 'улица Сезам'
        )

    def test_habit_list(self):
        url = reverse('habits:habits-list')
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(), {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [{
                    'id': self.habit.pk,
                    'place': 'place',
                    'start_time': '17:27:00',
                    'action': 'action',
                    'is_pleasant': True,
                    'periodicity': 2,
                    'prize': None,
                    'action_time': '00:02:00',
                    'is_public': True,
                    'user': self.user.pk,
                    'connected_habit': None
                }]
            }
        )

    def test_habit_delete(self):
        url = reverse('habits:habits-detail', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.all().count(), 0
        )
