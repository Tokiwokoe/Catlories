from django.urls import path
from meals import views
from meals.views import GetMealsByDate

urlpatterns = [
    path('meals', views.diary, name='diary'),
    path('add_meal', views.add_meal, name='add_meal'),
    path('get_meals/<str:date_str>/', GetMealsByDate.as_view(), name='get_meals_by_date'),
]
