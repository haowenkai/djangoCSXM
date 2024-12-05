"""
URL configuration for property_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views  # 确保导入了您的视图

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # 确保将根 URL 映射到您的视图
    path('house_management/', views.house_management, name='house_management'),
    path('fee_management/', views.fee_management, name='fee_management'),
    path('report_management/', views.report_management, name='report_management'),
    path('repair_management/', views.repair_management, name='repair_management'),
    path('announcement/', views.announcement, name='announcement'),
    path('property_management/', views.property_management, name='property_management'),
    path('permission_management/', views.permission_management, name='permission_management'),
]
