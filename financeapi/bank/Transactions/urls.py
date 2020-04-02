from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from Transactions import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'records', views.RecordViewSet)
router.register(r'admins', views.AdminViewSet)

# The API URLs are now determined automatically by the router.

urlpatterns = [

    path('', include(router.urls)),
   
]
