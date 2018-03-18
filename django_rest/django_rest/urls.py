"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from rest_framework import routers
from api import views

from rest_auth.views import (
    LoginView
)

from rest_auth.registration.views import (
    RegisterView
)
router= routers.DefaultRouter()
router.register('users', views.UserViewSet, 'user')





urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('register/', RegisterView.as_view(), name='rest_register'),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]

urlpatterns += router.urls
