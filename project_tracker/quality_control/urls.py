from django.urls import path
from quality_control import views

app_name = 'quality_control'



urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    path('home/', views.HomeView.as_view(), name='home_cbv'),
    path('bug-reports/', views.bug_report_list, name='bug_report_list'),
    path('bug-reports/<int:pk>/', views.BugReportDetailView.as_view(), name='bug_report_detail'),
    path('feature-requests/', views.feature_request_list, name='feature_request_list'),
    path('feature-requests/<int:pk>/', views.FeatureRequestDetailView.as_view(), name='feature_request_detail'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('inspections/', views.InspectionListView.as_view(), name='inspection_list'),
    path('feature-request/create/', views.feature_request_create, name='feature_request_create'),
    path('bug-reports/', BugReportListView.as_view(), name='bug_report_list'),
    path('bug-reports/<int:pk>/', BugReportDetailView.as_view(), name='bug_report_detail'),
    path('bug-reports/create/', BugReportCreateView.as_view(), name='bug_report_create'),
    path('bug-reports/<int:pk>/update/', BugReportUpdateView.as_view(), name='bug_report_update'),
    path('bug-reports/<int:pk>/delete/', BugReportDeleteView.as_view(), name='bug_report_delete'),path('feature-requests/', FeatureRequestListView.as_view(), name='feature_request_list'),
    path('feature-requests/<int:pk>/', FeatureRequestDetailView.as_view(), name='feature_request_detail'),
    path('feature-requests/create/', FeatureRequestCreateView.as_view(), name='feature_request_create'),
    path('feature-requests/<int:pk>/update/', FeatureRequestUpdateView.as_view(), name='feature_request_update'),
    path('feature-requests/<int:pk>/delete/', FeatureRequestDeleteView.as_view(), name='feature_request_delete'),
    path('inspections/<int:inspection_id>/', views.InspectionDetailView.as_view(), name='inspection_detail')
]


