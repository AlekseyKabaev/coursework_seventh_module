from celery import shared_task
from datetime import datetime

from habits.models import Habit
from habits.services import send_tg_message


@shared_task
def send_habit_message_of_tg():
    """Отправляет сообщение пользователю для напоминания о том, в какое время какие привычки необходимо выполнять."""
    habits = Habit.objects.all()
    current_time = datetime.now().time()
    for habit in habits:
        if habit.time >= current_time:
            chat_id = habit.user.tg_chat_id
            message = f'Напоминаем о необходимости выполнения {habit.action} в {habit.time}, место выполнения {habit.place}.'
            send_tg_message(chat_id, message)
