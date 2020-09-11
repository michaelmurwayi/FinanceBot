from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home" ),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.AccountView.as_view(), name='profile')
]
