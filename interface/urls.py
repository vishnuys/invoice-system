"""interface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic.base import RedirectView
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', RedirectView.as_view(url='/login/', permanent=True)),
    path('login/', views.LoginPage.as_view()),
    path('signup/', views.SignUpPage.as_view()),
    path('', views.HomePage.as_view()),
    path('dashboard/', views.DashboardPage.as_view()),
    path('logout/', views.LogoutPage.as_view()),
    path('dashboard/admin/', views.AdminPage.as_view()),
    path('dashboard/user/', views.UserPage.as_view()),
]
