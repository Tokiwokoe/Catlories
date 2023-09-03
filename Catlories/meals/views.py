from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Favorite
from .services import _add_to_favorite, _delete_favorite, _find_ingredient_by_code, _add_ingredient_in_diary, \
    _get_meals_by_date


class FavoritesListView(ListView):
    """List all food added to favorites"""
    model = Favorite
    paginate_by = 100

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        return context


class GetMealsByDate(APIView):
    """List all food added on selected date"""
    def get(self, request, date_str) -> Response:
        serializer = _get_meals_by_date(date_str=date_str, user_id=request.user.id)
        return Response(serializer.data, status=status.HTTP_200_OK) if serializer else Response(
            {'error': 'Wrong date'}, status=status.HTTP_400_BAD_REQUEST)


def ingredient_search_by_code(request, meal_type: int, date: str) -> HttpResponseRedirect:
    """Find an ingredient by its unique code"""
    code = request.GET.get('code')
    context = _find_ingredient_by_code(request=request, code=code, meal_type=meal_type, date=date)
    return render(request, 'meals/ingredient_page.html', context)


def add_ingredient_in_diary(request, meal_type: int, date: str, code: int) -> HttpResponseRedirect:
    """Add ingredient in a selected meal type and date"""
    grams = request.GET.get('grams')
    user_id = request.user.id
    _add_ingredient_in_diary(meal_type=meal_type, date=date, code=code, grams=grams, user_id=user_id)
    return HttpResponseRedirect(reverse('diary'))


def delete_from_favorite_list(request, id: int) -> HttpResponseRedirect:
    """Remove a food product from favorite list"""
    _delete_favorite(favorite_id=id)
    return HttpResponseRedirect(reverse('favorite_list'))


def add_to_favorite_list(request, code: int) -> HttpResponseRedirect:
    """Add a food product from favorite list"""
    user_id = request.user.id
    _add_to_favorite(code=code, user_id=user_id)
    return HttpResponseRedirect(reverse('favorite_list'))


def diary(request):
    """Render food diary page"""
    return render(request, 'meals/diary.html')


def add_meal(request):
    """Render page to search and add meals"""
    context = {'meal_type': request.GET.get('meal_type'),
               'date': request.GET.get('date')}
    return render(request, 'meals/add_meal.html', context)
