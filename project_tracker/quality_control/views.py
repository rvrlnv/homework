from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Система контроля качества<br><a href='/quality_control/bugs/'>Список всех багов</a><br><a href='/quality_control/features/'>Запросы на улучшение</a>")

def bug_list(request):
    return HttpResponse("Cписок отчетов об ошибках")

def feature_list(request):
    return HttpResponse("Список запросов на улучшение")

def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")

def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")

from django.shortcuts import render
from django.views.generic import DetailView
from .models import BugReport, FeatureRequest

# Function-Based Views для главной страницы приложения quality_control
def home(request):
    return render(request, 'quality_control/home.html')

# Class-Based Views для главной страницы приложения quality_control
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'quality_control/home.html'

# Function-Based Views для списка BugReport
def bug_report_list(request):
    bug_reports = BugReport.objects.all()
    return render(request, 'quality_control/bug_report_list.html', {'bug_reports': bug_reports})

# Class-Based Views для деталей BugReport
class BugReportDetailView(DetailView):
    model = BugReport
    template_name = 'quality_control/bug_report_detail.html'

# Function-Based Views для списка FeatureRequest
def feature_request_list(request):
    feature_requests = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_request_list.html', {'feature_requests': feature_requests})

# Class-Based Views для деталей FeatureRequest
class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    template_name = 'quality_control/feature_request_detail.html'