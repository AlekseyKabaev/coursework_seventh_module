from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('user', 'place', 'time', 'action', 'is_pleasant', 'related_habit', 'reward', 'is_public')
    list_filter = ('user', 'action', 'related_habit', 'reward')
    search_fields = ('user', 'place', 'time', 'action', 'related_habit', 'reward')
