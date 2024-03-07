from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('courses/', views.courses_page, name='courses'),
    path('contact/', views.contact_view, name='contact'),
    path('form_success', views.form_success, name='form_success'),
]
