from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('tasks/', include('tasks.urls')), 
# ]

urlpatterns = [
     path("admin/", admin.site.urls),
     path('', include('quality_control.urls')), 
 ]