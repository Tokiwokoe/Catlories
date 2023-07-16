from django.shortcuts import render


def index(request):
    return render(request, 'progress_analyzer/index.html')


def bmi_calculation(weight: float, height: int):
    """ Расчет индекса массы тела """
    bmi = weight / ((height / 100) ** 2)
    return bmi


def calories_calculation(weight: float, height: int, sex: str, activity_level: str, age: int):
    """ Подсчет рекоммендуемого количества калорий в сутки """
    pac = 0  # коэффициент физической активности (physical activity coefficient)
    calories = 0  # оптимальное кол-во калорий

    if activity_level == 'Низкий':
        pac = 1.4
    elif activity_level == 'Средний':
        pac = 1.6
    elif activity_level == 'Высокий':
        pac = 1.9
    elif activity_level == 'Очень высокий':
        pac = 2.2

    if sex == 'Мужской':
        calories = 66 + (13.7 * weight) + (5 * height) - (6.76 * age) * pac
    elif sex == 'Женский':
        calories = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age) * pac

    return calories
