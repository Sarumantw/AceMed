from django.shortcuts import render
from .models import question
from django.http import JsonResponse
import random
# Create your views here.
def quiz_view(request, subject):
    topic = request.GET.get('topic')
    first_question = question.objects.filter(subject=subject,topic =topic).first()
    return render(request, 'allqs.html', {'question': first_question, 'subject': subject, 'topic': topic})
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
def topic_index(request, subject):
    topics = question.objects.filter(subject = subject).values_list('topic', flat=True).distinct()
    return render(request, 'topic_index.html', {'topics': topics, 'subject': subject})



def next_question(request, subject, questionId, topic): 
    next_q = question.objects.filter(subject=subject, topic=topic, id__gt=questionId).first()

    if not next_q:
        return JsonResponse({'end': True})  # Ensure no crash if no next question

    # Create a dictionary mapping answer letters to their text
    choice_map = {
        'A': next_q.option1,
        'B': next_q.option2,
        'C': next_q.option3,
        'D': next_q.option4
    }

    # Extract choices as tuples (letter, text)
    choices = list(choice_map.items())

    # Shuffle the answer choices
    random.shuffle(choices)

    # Get the **correct answer's text** from the original stored letter
    correct_text = choice_map[next_q.answer]  

    # Find the **new letter** for the correct answer after shuffling
    correct_letter = next(letter for letter, text in choices if text == correct_text)

    return JsonResponse({
        'id': next_q.id,
        'question_text': next_q.question_text,
        'options': {letter: text for letter, text in choices},  # Send shuffled choices
        'answer': correct_letter,  # Send updated correct letter
        'topic': next_q.topic
    })

