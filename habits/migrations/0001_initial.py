# Generated by Django 5.1.2 on 2024-10-23 18:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='Место выполнения привычки')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Время выполнения привычки')),
                ('action', models.CharField(max_length=150, verbose_name='Полезная привычка / Действие')),
                ('is_pleasant', models.BooleanField(default=True, verbose_name='Признак приятной привычки')),
                ('periodicity', models.PositiveIntegerField(default=1, verbose_name='Периодичность (в днях)')),
                ('reward', models.CharField(blank=True, max_length=150, null=True, verbose_name='Приятная привычка / Вознаграждение')),
                ('execution_time', models.DurationField(blank=True, null=True, verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=True, verbose_name='Признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='Связанная привычка')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
