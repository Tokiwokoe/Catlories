from django.urls import path
from meals import views


urlpatterns = [
    path('meals', views.diary, name='diary'),
]