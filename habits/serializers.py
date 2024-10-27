from rest_framework import serializers

from habits.models import Habit
from habits.validators import ExcludeJointChoiceValidator, TimeDurationValidator, PleasantHabitValidator, \
    AbsenceValidator, FrequencyValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, attrs):
        # Инициализация валидаторов
        validators = [ExcludeJointChoiceValidator(), TimeDurationValidator(), PleasantHabitValidator(),
                      AbsenceValidator(), FrequencyValidator()]

        # Вызов валидаторов
        for validator in validators:
            validator(attrs)

        return attrs
