from django.shortcuts import render


def diary(request):
    return render(request, 'meals/diary.html')
