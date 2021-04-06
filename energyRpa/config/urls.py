"""HeatTransCo URL Configuration

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
from apps.calculator.views import *
from apps.common.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('signin/', auth_views.LoginView.as_view(), name='login'),
    path('signout/', auth_views.LogoutView.as_view(), name='logout'),
    path('calcs/', uvalue_calcs),
    #path('calcs/uvalue/<int:question_id>', uvalue_calcs)
    path('calcs/uvalue/data/', uvalue_data),
    path('calcs/uvalue/report/', uvalue_report),
    path('calcs/uvalue/post/', uvalue_save)
]

