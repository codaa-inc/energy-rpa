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
    path('signin/', signin),
    path('signout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', index),
    path('calcs/', calcs),
    path('calcs/uvalue', uvalue_init_calcs),
    path('calcs/uvalue/<int:uvalue_tmpl_cd>', uvalue_user_calcs),
    path('calcs/uvalue/data/<int:id>', uvalue_user_calcs_res),
    path('calcs/uvalue/initdata', uvalue_data),
    path('calcs/uvalue/report', uvalue_report),
    path('calcs/uvalue/post', uvalue_save)
]

