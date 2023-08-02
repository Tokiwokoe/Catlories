from django.urls import path
from meals import views
from meals.views import GetMealsByDate, IngredientSearchView, AddIngredientView, AddToFavoritesView

urlpatterns = [
    path('', views.diary, name='diary'),
    path('add_meal/', views.add_meal, name='add_meal'),
    path('get_meals/<str:date_str>/', GetMealsByDate.as_view(), name='get_meals_by_date'),
    path('ingredient_search/meal_type=<str:meal_type>&date=<date>', IngredientSearchView.as_view(), name='ingredient_search'),
    path('add_ingredient/meal_type=<str:meal_type>&date=<date>&code=<code>', AddIngredientView.as_view(), name='add_ingredient'),
    path('add_to_favorites/code=<int:code>', AddToFavoritesView.as_view(), name='add_to_favorites'),
]
