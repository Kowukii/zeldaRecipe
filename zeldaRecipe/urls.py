"""
URL configuration for zeldaRecipe project.

The `urlpatterns` list routes URLs to bank. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function bank
    1. Add an import:  from my_app import bank
    2. Add a URL to urlpatterns:  path('', bank.home, name='home')
Class-based bank
    1. Add an import:  from other_app.bank import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.bank import *
urlpatterns = [
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path("admin/", admin.site.urls),
]
