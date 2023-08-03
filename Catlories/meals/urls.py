from django.urls import path
from meals import views
from meals.views import (
    add_ingredient_in_diary,
    add_to_favorite_list,
    delete_from_favorite_list,
    FavoritesListView,
    GetMealsByDate,
    ingredient_search_by_code
)


urlpatterns = [
    path('', views.diary, name='diary'),
    path('add_meal/', views.add_meal, name='add_meal'),
    path('get_meals/<str:date_str>/', GetMealsByDate.as_view(), name='get_meals_by_date'),
    path('ingredient_search/meal_type=<str:meal_type>&date=<date>', ingredient_search_by_code,
         name='ingredient_search'),
    path('add_ingredient/meal_type=<str:meal_type>&date=<date>&code=<code>', add_ingredient_in_diary,
         name='add_ingredient'),
    path('add_to_favorites/code=<int:code>', add_to_favorite_list, name='add_to_favorites'),
    path('favorites/', FavoritesListView.as_view(), name='favorite_list'),
    path('delete_favorite/<int:id>', delete_from_favorite_list, name='delete_favorite'),
]
