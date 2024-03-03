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
            # smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            # smtpObj.starttls()
            # smtpObj.login('vadikschool248@gmail.com', 'vadyusha5')

            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            # smtpObj.sendmail('vadikschool248@gmail.com', email, f'Hello, {name}! {message}')
            # smtpObj.quit()
            send_mail(
                "Welcome!",
                f'{name} is new user! His/her email: {email} \nMessage:\n{message}',
                'rucodinger@yandex.ru',
                ['rucodinger@gmail.com'],
                fail_silently=False,
            )

            return render(request, 'form_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html')
