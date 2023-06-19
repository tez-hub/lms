from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('courses/', courses, name='courses'),
    path('course/<int:pk>/', course, name='course'),
    path('lesson/', lesson, name='lesson'),
    path('profile', profile, name='profile')
]