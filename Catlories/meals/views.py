from django.shortcuts import render


def diary(request):
    return render(request, 'meals/diary.html')


def add_meal(request):
    return render(request, 'meals/add_meal.html')
