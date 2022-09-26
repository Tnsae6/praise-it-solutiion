"""Praise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from post.views import *
from contact.views import *
from about.views import *
from service.views import *
from shop.views import *
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import *
from django.contrib import admin
from django.urls import path

app_name = 'contact'
app_name = 'post'
app_name = 'about'
app_name = 'shop'
app_name = 'service'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index" ),
    path('index.html', index, name="index"),
    path('contact.html', contact, name="contact"),
    path('service.html/<id>', service , name="choose_service"),
    path('service.html', service, name="service"),
    path('about.html', about, name="about"),
    path('shop.html', shop, name="shop"),
    path('team.html', team, name="team"),
    path('faq.html', faq, name="faq"),

]

handle404 = 'post.views.page404'

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
