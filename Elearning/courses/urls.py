from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.Courses, name='Courses'),
    path('courses/', views.Student, name='Students'),
]