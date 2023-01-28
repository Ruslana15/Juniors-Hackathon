from django.urls import path

from .views import *



urlpatterns = [
    path('vacancy/', VacancyAPIView.as_view()),
    path('vacancy/<str:pk>/', VacancyAPIView.as_view()),
]
