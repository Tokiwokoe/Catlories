from django.shortcuts import render


def index(request):
    return render(request, 'progress_analyzer/index.html')


def bmi_calculation(weight: float, height: int):
    """ Calculates body mass index  """
    bmi = weight / ((height / 100) ** 2)
    return bmi


def calories_calculation(weight: float, height: int, sex: int, activity_level: int, age: int):
    """ Calculates recommended daily calories """
    pac = 0  # physical activity coefficient
    cal = 0  # optimal daily calories

    if activity_level == 1:
        pac = 1.4
    elif activity_level == 2:
        pac = 1.6
    elif activity_level == 3:
        pac = 1.9
    elif activity_level == 4:
        pac = 2.2

    if sex == 1:
        cal = 66 + (13.7 * weight) + (5 * height) - (6.76 * age) * pac
    elif sex == 2:
        cal = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age) * pac

    return cal
