from django.urls import path
from quality_control import views

app_name = 'quality_control'



urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    path('', views.home, name='home'),
    path('home/', views.HomeView.as_view(), name='home_cbv'),
    path('bug-reports/', views.bug_report_list, name='bug_report_list'),
    path('bug-reports/<int:pk>/', views.BugReportDetailView.as_view(), name='bug_report_detail'),
    path('feature-requests/', views.feature_request_list, name='feature_request_list'),
    path('feature-requests/<int:pk>/', views.FeatureRequestDetailView.as_view(), name='feature_request_detail')
]


