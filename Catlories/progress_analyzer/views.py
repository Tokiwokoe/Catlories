from django.shortcuts import render
from datetime import date


def index(request):
    if request.user.is_authenticated:
        context = {'cal': calories_calculation(weight=float(request.user.profile.weight_kg),
                                               height=int(request.user.profile.height_cm),
                                               sex=str(request.user.profile.sex),
                                               activity_level=str(request.user.profile.activity_level),
                                               age=int(date.today().year - request.user.profile.birth_date.year)),
                   'bmi': bmi_calculation(weight=request.user.profile.weight_kg,
                                          height=request.user.profile.height_cm)}
    else:
        context = {}
    return render(request, 'progress_analyzer/index.html', context)


def bmi_calculation(weight: float, height: int) -> str:
    """ Calculates body mass index """
    bmi = "{:.1f}".format(weight / ((height / 100) ** 2))
    return bmi


def calories_calculation(weight: float, height: int, sex: str, activity_level: str, age: int) -> int:
    """ Calculates recommended daily calories """
    pac = 0  # physical activity coefficient
    cal = 0  # optimal daily calories

    if activity_level == 'Низкий':
        pac = 1.4
    elif activity_level == 'Средний':
        pac = 1.6
    elif activity_level == 'Высокий':
        pac = 1.9
    elif activity_level == 'Очень высокий':
        pac = 2.2

    if sex == 'Мужской':
        cal = int(66 + (13.7 * weight) + (5 * height) - (6.76 * age))
    elif sex == 'Женский':
        cal = int(655 + (9.6 * weight) + (1.8 * height) - (4.7 * age) * pac)

    return cal
