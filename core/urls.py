"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.home import urls as home_url
from apps.companies import urls as company_url
from apps.departments import urls as departament_url
from apps.documents import urls as document_url
from apps.employees import urls as employee_url
from apps.overtimes import urls as overtimes_url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include(home_url)),
    path('admin/', admin.site.urls),
    path('companies/', include(company_url)),
    path('departments/', include(departament_url)),
    path('documents/', include(document_url)),
    path('employees/', include(employee_url)),
    path('overtimes/', include(overtimes_url)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
