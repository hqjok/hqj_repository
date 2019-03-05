"""uni_forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from forum import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('index/', views.index),
    path('login_test/', views.login_test),
    path('check_user/', views.check_user),
    re_path(r'^media/(.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^captcha', include('captcha.urls')),
    path('logout/', views.logout),
    path('reception/', include('reception.urls'))
]
