from django.shortcuts import render
from django.core.mail import send_mail
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

            send_mail(
                "New client",
                f'{name} is our new client! \nEmail: {email} \n\nMessage:\n{message}',
                'rucodinger@yandex.ru',
                ['rucodinger@gmail.com'],
                fail_silently=False,
            )

            return render(request, 'form_success.html')
    return render(request, 'contact.html')