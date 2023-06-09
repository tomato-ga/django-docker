from django.contrib import admin
from .models import Project, TodoModel

class TodoModelInline(admin.TabularInline):
    model = TodoModel
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [TodoModelInline]
    list_display = ['name']

class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'updated_at', 'created_at']  # タスクのタイトルとプロジェクト名を表示

admin.site.register(Project, ProjectAdmin)
admin.site.register(TodoModel, TodoModelAdmin)
