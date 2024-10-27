from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='Место выполнения привычки')
    time = models.TimeField(verbose_name='Время выполнения привычки')
    action = models.CharField(max_length=150, verbose_name='Полезная привычка / Действие')
    is_pleasant = models.BooleanField(default=True, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE)
    periodicity = models.PositiveIntegerField(default=1, verbose_name='Периодичность (в днях)')
    reward = models.CharField(max_length=150, verbose_name='Приятная привычка / Вознаграждение', **NULLABLE)
    execution_time = models.DurationField(verbose_name='Время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=True, verbose_name='Признак публичности')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f'Действие {self.action} ({self.user})'
