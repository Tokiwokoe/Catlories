from django.db import models
from psqlextra.indexes import UniqueIndex
from profiles.models import Profile


class Ingredient(models.Model):
    class Meta:
        indexes = [
            UniqueIndex(fields=['name']),
        ]

    name = models.CharField(max_length=128)
    kcal_per_100g = models.IntegerField()
    carbs_per_100g = models.FloatField()
    protein_per_100g = models.FloatField()
    fat_per_100g = models.FloatField()

    def __str__(self):
        return self.name


class MealType(models.Model):
    class Meta:
        indexes = [
            UniqueIndex(fields=['name']),
        ]

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Meal(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE)
    dish = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    grams = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.meal_type}, {self.dish}, {self.date}'
