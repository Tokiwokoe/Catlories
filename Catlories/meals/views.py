from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meal
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


def diary(request):
    return render(request, 'meals/diary.html')


def add_meal(request):
    return render(request, 'meals/add_meal.html')
