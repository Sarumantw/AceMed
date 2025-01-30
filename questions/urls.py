from django.urls import path
from . import views

urlpatterns = [
    path('allquestions/', views.quiz_view, name='quiz_view'),
    path('check_answers/', views.check_answers, name='check_answers'),
]