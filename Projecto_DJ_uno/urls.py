"""Projecto_DJ_uno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Projecto_DJ_uno.views import welcome, welcomeRed, ageCategory, getCurrentdate, contentHTML, firtstemplate, templateParameters, templateLoader

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Welcome/', welcome),
    path('WelcomeRed/', welcomeRed),
    path('AgeCategory/<int:age>', ageCategory),
    path('GetDate/', getCurrentdate),
    path('ContentHTML/<name>/<int:age>', contentHTML),
    path('FirtsTem/', firtstemplate),
    path('TemplateParameters/', templateParameters),
    path('TemplateLoarder/', templateLoader)
]
