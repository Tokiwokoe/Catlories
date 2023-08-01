from django.core.handlers import exception
from django.shortcuts import render
from django.views import View, defaults
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meal, Ingredient
from .serializers import MealSerializer
from datetime import datetime


class GetMealsByDate(APIView):
    def get(self, request, date_str):
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            meals = Meal.objects.filter(date=date, user_id=request.user.id)
            serializer = MealSerializer(meals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Неверная дата'}, status=status.HTTP_400_BAD_REQUEST)


class IngredientSearchView(View):
    def get(self, request):
        code = request.GET.get('code', None)
        meal_type = request.GET.get('meal_type', None)
        date = request.GET.get('date', None)
        if code:
            try:
                context = {}
                ingredient = Ingredient.objects.get(code=code)
                context['name'] = ingredient.name
                context['kcal_per_100g'] = ingredient.kcal_per_100g
                context['carbs_per_100g'] = ingredient.carbs_per_100g
                context['protein_per_100g'] = ingredient.protein_per_100g
                context['fat_per_100g'] = ingredient.fat_per_100g
                print(meal_type, date)
                return render(request, 'meals/ingredient_page.html', context)
            except Ingredient.DoesNotExist:
                return defaults.page_not_found(request, exception, template_name='404.html')
        else:
            return defaults.page_not_found(request, exception, template_name='404.html')


def diary(request):
    return render(request, 'meals/diary.html')


def add_meal(request):
    return render(request, 'meals/add_meal.html')
