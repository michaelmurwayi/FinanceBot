"""bank URL Configuration

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
from django.urls import path, include
<<<<<<< HEAD
from django.conf.urls import include
from Accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Accounts.url')),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.api_root),

=======
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Accounts.url'))
=======


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Accounts.url')),
>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b
]
