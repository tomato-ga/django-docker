from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


CHOISE = (('danger','high'), ('warning','normal'), ('primary', 'low'))

class TodoModel(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', default=1)
    title = models.CharField(max_length=255)
    memo = models.TextField()
    updated_at = models.DateTimeField('更新日', auto_now=True)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    priority = models.CharField(max_length=100, choices=CHOISE)
    duedate = models.DateTimeField()
    
    
    def __str__(self) -> str:
        return self.title
    
