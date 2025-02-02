from django.shortcuts import render
from .models import question
# Create your views here.
def quiz_view(request, subject):
    questions = question.objects.filter(subject=subject)
    return render(request, 'allqs.html', {'questions': questions, 'subject': subject})
def check_answers(request):
    if request.method == 'POST':
        questions = question.objects.all()
        score = 0
        for q in questions:
            if request.POST.get("q"+str(q.id)) == q.answer:
                score += 1
        return render(request, 'results', {'score': score})
def homepage(request):
    return render(request, 'main.html')