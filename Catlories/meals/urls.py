from django.urls import path
from meals import views


urlpatterns = [
    path('meals', views.diary, name='diary'),
    path('add_meal', views.add_meal, name='add_meal'),
]
