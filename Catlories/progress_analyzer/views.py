from django.shortcuts import render


def index(request):
    return render(request, 'progress_analyzer/index.html')
