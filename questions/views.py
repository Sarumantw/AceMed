from django.shortcuts import render
from .models import question
from django.http import JsonResponse
# Create your views here.
def quiz_view(request, subject):
    first_question = question.objects.filter(subject=subject).first()
    return render(request, 'allqs.html', {'questions': first_question, 'subject': subject})
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
def next_question(request, subject, q_id):
        next_q = question.objects.filter(subject = subject, id__gt = q_id).first()
        if next_q:
            return JsonResponse({
                'id' : next_q.id,
                'question_text' : next_q.question_text,
                'option1' : next_q.option1,
                'option2' : next_q.option2,
                'option3' : next_q.option3,
                'option4' : next_q.option4,
                'answer' : next_q.answer })
        else: 
           return JsonResponse({
               'end' : True })
