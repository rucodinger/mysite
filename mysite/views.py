from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from .forms import ContactForm


def home_page(request):
    return render(request, 'index.html')


def courses_page(request):
    return render(request, 'courses.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            print(name, email, message)
            return render(request, 'form_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html')

# def contact_view(request):
#     return render(request, 'contact.html')
