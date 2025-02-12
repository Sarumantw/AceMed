from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<str:subject>', views.quiz_view, name='quiz_view'),
    path('check_answers/', views.check_answers, name='check_answers'),
    path('quiz/<str:subject>/<str:topic>/next/<int:questionId>/', views.next_question, name= 'next_question'),
    path('topics/<str:subject>/', views.topic_index, name='topic_index'),
]
