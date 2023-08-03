from django.core.handlers import exception
from django.http import JsonResponse
from django.utils.datetime_safe import datetime
from django.views import defaults
from meals.models import Ingredient, Favorite, Meal, MealType
from meals.serializers import MealSerializer


def _add_to_favorite(code: int, user_id: int) -> JsonResponse:
    dish_id = Ingredient.objects.get(code=code)
    if not Favorite.objects.filter(user_id=user_id, ingredient=dish_id):
        fav = Favorite(user_id=user_id, ingredient=dish_id)
        fav.save()
    return JsonResponse({'success': True})


def _delete_favorite(favorite_id: int) -> JsonResponse:
    fav = Favorite.objects.get(id=favorite_id)
    fav.delete()
    return JsonResponse({'success': True})


def _find_ingredient_by_code(request, code: int, meal_type: int, date: str) -> dict:
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
            return context
        except Ingredient.DoesNotExist:
            return defaults.page_not_found(request, exception, template_name='404.html')
    else:
        return defaults.page_not_found(request, exception, template_name='404.html')


def _add_ingredient_in_diary(meal_type: int, date: str, code: int, grams: int, user_id: int) -> None:
    meal_type_id = MealType.objects.get(id=meal_type)
    dish_id = Ingredient.objects.get(code=code)
    meal = Meal.objects.filter(user_id=user_id, meal_type=meal_type_id, dish=dish_id, date=date)
    if meal:
        meal = Meal.objects.get(user_id=user_id, meal_type=meal_type_id, dish=dish_id, date=date)
        meal.grams = meal.grams + int(grams)
    else:
        meal = Meal(user_id=user_id, meal_type=meal_type_id, dish=dish_id, grams=grams, date=date)
    meal.save()


def _get_meals_by_date(date_str: str, user_id: int) -> MealSerializer:
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    meals = Meal.objects.filter(date=date, user_id=user_id)
    serializer = MealSerializer(meals, many=True)
    return serializer
