from django.urls import path
from Transactions import views

urlpatterns = [
    path('records/', views.records_list),
    path('records/<int:pk>/', views.record_detail),
]