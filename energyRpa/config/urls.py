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


    # common urls
    path('', index),
    path('admin/', admin.site.urls),
    path('signin/', signin),
    path('signout/', auth_views.LogoutView.as_view(), name='logout'),
    path('calcs/', list),
    path('project/', insert_project),

    # calculator urls
    path('calcs/uvalue', init_uvalue),
    path('calcs/uvalue/<int:uvalue_tmpl_cd>', get_user_uvalue),
    path('calcs/uvalue/select/<int:id>', select_uvalue),
    path('calcs/uvalue/insert', insert_uvalue),
    path('calcs/uvalue/update/<int:id>', update_uvalue),
    path('calcs/uvalue/data', load_data_uvalue),
    path('calcs/uvalue/report/<int:uvalue_tmpl_cd>', report_uvalue),
]

