from django.shortcuts import render
from .models import question
# Create your views here.
def quiz_view(request):
    questions = question.objects.all()
    return render(request, 'allqs.html', {'questions': questions})
def check_answers(request):
    if request.method == 'POST':
        questions = question.objects.all()
        score = 0
        for q in questions:
            if request.POST.get("q"+str(q.id)) == q.answer:
                score += 1
        return render(request, 'results', {'score': score})