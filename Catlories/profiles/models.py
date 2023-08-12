from django.db import models
from psqlextra.indexes import UniqueIndex
from django.contrib.auth.models import User


class Sex(models.Model):
    class Meta:
        indexes = [
            UniqueIndex(fields=['name']),
        ]

    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class ActivityLevel(models.Model):
    class Meta:
        indexes = [
            UniqueIndex(fields=['name']),
        ]

    name = models.CharField(max_length=15, unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Goal(models.Model):
    class Meta:
        indexes = [
            UniqueIndex(fields=['name']),
        ]

    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/uploads', verbose_name='Аватар')
    name = models.CharField(max_length=20, verbose_name='Имя')
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, verbose_name='Пол')
    birth_date = models.DateField(verbose_name='Дата рождения')
    weight_kg = models.FloatField(verbose_name='Вес (кг)')
    height_cm = models.IntegerField(verbose_name='Рост (см)')
    activity_level = models.ForeignKey(ActivityLevel, on_delete=models.CASCADE, verbose_name='Уровень активности')
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, verbose_name='Цель')

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
