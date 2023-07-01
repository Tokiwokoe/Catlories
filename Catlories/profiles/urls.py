from django.urls import path
from .views import ProfileView, UpdateProfile

urlpatterns = [
    path('<str:username>/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/update/', UpdateProfile.as_view(), name='update_profile'),
]