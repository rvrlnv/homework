from django.http import HttpResponse
from django.urls import reverse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.shortcuts import render

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')
    
class ProjectsListView(ListView):
    model = Project
    template_name = 'tasks/projects_list.html'

class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'
    template_name = 'tasks/project_detail.html'

class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/task_detail.html'

def index(request):
    return render(request, 'tasks/index.html')

def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/projects_list.html', {'project_list': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'tasks/project_detail.html', {'project': project})

def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    return render(request, 'tasks/task_detail.html', {'task': task})