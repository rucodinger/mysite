from django.shortcuts import render


def home_page(request):
    return render(request, 'index.html')


def courses_page(request):
    return render(request, 'courses.html')
