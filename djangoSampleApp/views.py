from django.http import HttpResponse
from django.views.generic import TemplateView


# # requestオブジェクトを受け取る　名前はなんでもいい
# def helloworldfunction(request):
#     returnobject = HttpResponse('<h1>hello world!!</h1>')
#     return returnobject


# class HelloworldClass(TemplateView):
#     template_name = 'hello.html'

from pathlib import Path
from django.http import HttpResponse

def helloworldfunction(request):
    returnobject = HttpResponse('<h1>hello world></h1>')
    return returnobject

class HelloworldClass(TemplateView):
    template_name = 'hello.html'