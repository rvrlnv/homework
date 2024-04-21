from django.shortcuts import render, redirect
from .forms import BugReportForm, FeatureRequestForm
from django.http import HttpResponse
from django.views.generic import DetailView, TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import BugReport, FeatureRequest, Product


def index(request):
    return render(request, 'quality_control/index.html')

def bug_list(request):
    return HttpResponse("Cписок отчетов об ошибках")

def feature_list(request):
    return HttpResponse("Список запросов на улучшение")

def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")

def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")

# Function-Based Views для главной страницы приложения quality_control
def home(request):
    return render(request, 'quality_control/home.html')


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


class ProductListView(ListView):
    model = Product
    template_name = 'quality_control/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'quality_control/product_detail.html'
    pk_url_kwarg = 'product_id'

class InspectionListView(ListView):
    model = Inspection
    template_name = 'quality_control/inspection_list.html'

class InspectionDetailView(DetailView):
    model = Inspection
    template_name = 'quality_control/inspection_detail.html'
    pk_url_kwarg = 'inspection_id'

def bug_report_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = BugReportForm()
    return render(request, 'bug_report_form.html', {'form': form})

def feature_request_create(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = FeatureRequestForm()
    return render(request, 'feature_request_form.html', {'form': form})

def bug_report_detail(request, pk):
    bug_report = get_object_or_404(BugReport, pk=pk)
    return render(request, 'quality_control/bug_report_detail.html', {'bug_report': bug_report})

def bug_report_update(request, pk):
    bug_report = get_object_or_404(BugReport, pk=pk)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug_report)
        if form.is_valid():
            form.save()
            return redirect('bug_report_detail', pk=bug_report.pk)
    else:
        form = BugReportForm(instance=bug_report)
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def bug_report_delete(request, pk):
    bug_report = get_object_or_404(BugReport, pk=pk)

def feature_request_detail(request, pk):
    feature_request = get_object_or_404(FeatureRequest, pk=pk)
    return render(request, 'quality_control/feature_request_detail.html', {'feature_request': feature_request})

def feature_request_update(request, pk):
    feature_request = get_object_or_404(FeatureRequest, pk=pk)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature_request)
        if form.is_valid():
            form.save()
            return redirect('feature_request_detail', pk=feature_request.pk)
    else:
        form = FeatureRequestForm(instance=feature_request)
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

def feature_request_delete(request, pk):
    feature_request = get_object_or_404(FeatureRequest, pk=pk)
    if request.method == 'POST':
        feature_request.delete()
        return redirect('feature_request_list')
    return render(request, 'quality_control/feature_request_confirm_delete.html', {'feature_request': feature_request})

class BugReportListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_report_list.html'
    context_object_name = 'bug_reports'

class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('bug_report_list')

class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('bug_report_list')

class BugReportDeleteView(DeleteView):
    model = BugReport
    template_name = 'quality_control/bug_report_confirm_delete.html'
    success_url = reverse_lazy('bug_report_list')

class FeatureRequestListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_request_list.html'
    context_object_name = 'feature_requests'

class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('feature_request_list')

class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('feature_request_list')

class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    template_name = 'quality_control/feature_request_confirm_delete.html'
    success_url = reverse_lazy('feature_request_list')