from django.core.handlers import exception
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View, defaults
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meal, Ingredient, MealType, Favorite
from .serializers import MealSerializer
from datetime import datetime


def diary(request):
    return render(request, 'meals/diary.html')


def add_meal(request):
    context = {}
    context['meal_type'] = request.GET.get('meal_type', None)
    context['date'] = request.GET.get('date', None)
    return render(request, 'meals/add_meal.html', context)


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
    def get(self, request, meal_type, date):
        code = request.GET.get('code', None)
        if code:
            try:
                context = {}
                ingredient = Ingredient.objects.get(code=code)
                context['meal_type'] = meal_type
                context['date'] = date
                context['code'] = code
                context['name'] = ingredient.name
                context['kcal_per_100g'] = ingredient.kcal_per_100g
                context['carbs_per_100g'] = ingredient.carbs_per_100g
                context['protein_per_100g'] = ingredient.protein_per_100g
                context['fat_per_100g'] = ingredient.fat_per_100g
                return render(request, 'meals/ingredient_page.html', context)
            except Ingredient.DoesNotExist:
                return defaults.page_not_found(request, exception, template_name='404.html')
        else:
            return defaults.page_not_found(request, exception, template_name='404.html')


class AddIngredientView(APIView):
    def get(self, request, meal_type, date, code):
        meal_type_id = MealType.objects.get(id=meal_type)
        dish_id = Ingredient.objects.get(code=code)
        grams = request.GET.get('grams', None)
        meal = Meal.objects.filter(user_id=request.user.id, meal_type=meal_type_id, dish=dish_id, date=date)
        if meal:
            meal = Meal.objects.get(user_id=request.user.id, meal_type=meal_type_id, dish=dish_id, date=date)
            meal.grams = meal.grams + int(grams)
        else:
            meal = Meal(user_id=request.user.id, meal_type=meal_type_id, dish=dish_id, grams=grams, date=date)
        meal.save()
        return HttpResponseRedirect(reverse('diary'))


class AddToFavoritesView(APIView):
    def get(self, request, code):
        dish_id = Ingredient.objects.get(code=code)
        if not Favorite.objects.filter(user_id=request.user.id, ingredient=dish_id):
            fav = Favorite(user_id=request.user.id, ingredient=dish_id)
            fav.save()
        return HttpResponseRedirect(reverse('favorite_list'))


class FavoritesView(ListView):
    model = Favorite
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DeleteFavorite(APIView):
    def get(self, request, id):
        fav = Favorite.objects.get(id=id)
        fav.delete()
        return HttpResponseRedirect(reverse('favorite_list'))
