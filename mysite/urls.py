from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('/', views.home, name='index'),
    path('home/', views.home, name='index'),
    path('courses/', views.courses, name='courses'),
]
