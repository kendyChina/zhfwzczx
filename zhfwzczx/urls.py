"""zhfwzczx URL Configuration

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
from excel_factory import views as excel_factory_views

urlpatterns = [
    path(r"", excel_factory_views.index_redirect, name="index_red"),
    path(r"index", excel_factory_views.index, name="index"),
    path(r"insert_xsg", excel_factory_views.insert_xsg, name="insert_xsg"),
    path(r"insert_wyg", excel_factory_views.insert_wyg, name="insert_wyg"),
    path(r"insert_cz", excel_factory_views.insert_cz, name="insert_cz"),
    path(r"search_xsg", excel_factory_views.search_xsg, name="search_xsg"),
    path('admin/', admin.site.urls),

]
