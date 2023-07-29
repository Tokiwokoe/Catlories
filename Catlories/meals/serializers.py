from rest_framework import serializers
from .models import Meal, Ingredient, MealType


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class MealTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealType
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    dish = IngredientSerializer()
    meal_type = MealTypeSerializer()

    class Meta:
        model = Meal
        fields = 'dish', 'meal_type', 'date', 'grams'

