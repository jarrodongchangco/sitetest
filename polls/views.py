from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .forms import QuestionModelForm

# Create your views here.


def index(request):
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions
    return render(request, 'index.html', context)

def help(request):
    return HttpResponse('This is the help page')

def detail(request, question_id):
    context = {}
    context['question'] = Question.objects.get(id=question_id)
    return render(request, 'detail.html', context)

def update(request, question_id):
    if request.method == 'POST':
        pass
    else:
        question = Question.objects.get(id=question_id)
        context = {}
        context['form'] = QuestionModelForm(instance=question)
        return render(request, 'update.html', context)
