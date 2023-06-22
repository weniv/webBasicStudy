from django.shortcuts import render
from .models import Question, Developer, Choice

# Create your views here.

def index(request):
    developers = Developer.objects.all()
    
    print(developers.query)
    
    context = {
        'developers': developers,
    }
    
    return render(request, 'index.html', context = context)

def form(request):
    questions = Question.objects.all()
    
    context = {
        'questions': questions,
    }
    
    return render(request, 'form.html', context = context)

def result(request):
    
    #문항의 수
    N = Question.objects.count()
    
    #개발자 유형의 수     
    K = Developer.objects.count()
    
    counter = [0] * (K + 1)
    # counter == [0,0,0,0,0,0]
    
    print(f'POST : {request.POST}')
    #[1,2,3,4,5]     
    
    for n in range(1, N+1):
        try:
            developer_id = int(request.POST[f'question-{n}'][0])
            counter[developer_id] += 1
        except (KeyError, ValueError, IndexError):
            continue
        
    # counter == [0,3,4,0,6,0]
    best_developer_id = max(range(1, K+1), key=lambda id: counter[id])
    # [1,2,3,4,5]    
    best_developer =  Developer.objects.get(pk=best_developer_id)
    best_developer.count += 1
    best_developer.save()
    
    context = {
        'developer' : best_developer,
        'counter' : counter
    }
    
    return render(request, 'result.html', context)
