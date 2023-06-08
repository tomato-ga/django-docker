from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hello world polls')


def detail(request, question_id):
    return HttpResponse('youre looking at question' % question_id)

def results(request, question_id):
    response = 'Youre looking results'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('youre voting on question' % question_id)

