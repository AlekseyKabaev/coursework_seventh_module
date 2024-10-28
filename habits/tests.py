from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='new_test@test.ru')
        self.habit = Habit.objects.create(user=self.user, place='Earth', time="14:00:00", action='Тренеровка',
                                          is_pleasant=True, periodicity=3, execution_time='00:02:00', is_public=True)
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse('habits:habits-retrieve', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('place'), self.habit.place
        )

    def test_habit_create(self):
        url = reverse('habits:habits-create')
        data = {
            "user": self.user.pk,
            "place": "Спорт зал",
            "time": "14:00:00",
            "action": "Тренировка",
            "is_pleasant": True,
            "periodicity": 3,
            "execution_time": "00:02:00",
            "is_public": True
        }
        response = self.client.post(url, data)

        print(response.status_code)  # Печать статуса ответа
        print(response.json())  # Печать содержимого ответа для диагностики

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        print(response.content)
        self.assertEqual(
            Habit.objects.all().count(), 2
        )

    def test_habit_update(self):
        url = reverse('habits:habits-update', args=(self.habit.pk,))
        data = {
            "place": "Улица",
            'periodicity': 2,
        }
        response = self.client.patch(url, data)
        data = response.json()

        print(response.status_code)  # Печать статуса ответа
        print(response.json())  # Печать содержимого ответа для диагностики

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('place'), "Улица"
        )

    def test_habit_delete(self):
        url = reverse('habits:habits-delete', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.count(), 0
        )

    def test_habit_list(self):
        url = reverse('habits:habits-list_public')
        response = self.client.get(url)
        # data = response.json()

        print(response.json())  # Печать содержимого ответа для диагностики

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
