from rest_framework.serializers import ValidationError
from datetime import timedelta


class ExcludeJointChoiceValidator:
    """Валидация об исключении одновременного выбора связанной привычки и вознаграждения"""
    def __call__(self, habit):
        if habit.get("related_habit") and habit.get("reward"):
            raise ValidationError("Нельзя одновременно выбирать связанную привычку и вознаграждение!")


class TimeDurationValidator:
    """Валидация по времени выполнения привычки."""
    duration_time = timedelta(seconds=120)

    def __call__(self, habit):
        if habit.get("execution_time") and habit["execution_time"].total_seconds() > self.duration_time.total_seconds():
            raise ValidationError("Действие выполняется более 120 секунд!")


class PleasantHabitValidator:
    """Валидация попадания в связанные привычки только приятных привычек."""

    def __call__(self, habit):
        if habit.get("related_habit") and not habit["related_habit"].is_pleasant:
            raise ValidationError("Связанные привычки могут быть только приятными")


class AbsenceValidator:
    """Валидация по отсутствию у приятной привычки связанной привычки или вознаграждения."""

    def __call__(self, habit):
        if habit.get("is_pleasant"):
            if habit.get("related_habit") or habit.get("reward"):
                raise ValidationError(
                    "У приятной привычки не может быть связанной привычки или вознаграждения"
                )


class FrequencyValidator:
    """Валидация по частоте исполнения полезной привычки / действия."""

    def __call__(self, habit):
        if habit.get("periodicity") < 7:
            raise ValidationError("Привычку нельзя выполнять реже 1 раза в 7 дней.")
        if habit.get("periodicity") > 7:
            raise ValidationError("Привычку нельзя выполнять чаще 1 раза в 7 дней.")
