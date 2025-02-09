from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<str:subject>', views.quiz_view, name='quiz_view'),
    path('check_answers/', views.check_answers, name='check_answers'),
    path('quiz/<str:subject>/next/<int:qid>/', views.next_question, name= 'nextq'),
]
