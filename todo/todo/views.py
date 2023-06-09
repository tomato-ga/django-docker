from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView, UpdateView, CreateView

from .models import TodoModel
from django.urls import reverse_lazy

class Todolist(ListView):
    template_name = 'list.html'
    model = TodoModel
    
    
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
    
    
class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
    
    
class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list') # デリート↓後にどこに遷移するかを指定する
    
    
class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list') # デリート↓後にどこに遷移するかを指定する


