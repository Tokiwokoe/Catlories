from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meal, Ingredient
from .serializers import MealSerializer, IngredientSerializer
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


class IngredientSearchView(APIView):
    def get(self, request):
        code = request.GET.get('code', None)
        if code:
            try:
                ingredient = Ingredient.objects.get(code=code)
                serializer = IngredientSerializer(ingredient)
                return Response(serializer.data)
            except Ingredient.DoesNotExist:
                return Response({'detail': 'Продукт не найден'}, status=404)
        else:
            return Response({'detail': 'Введите штрих-код продукта'}, status=400)


def diary(request):
    return render(request, 'meals/diary.html')


def add_meal(request):
    return render(request, 'meals/add_meal.html')
