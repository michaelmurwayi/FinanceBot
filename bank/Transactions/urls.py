from django.urls import path
from Transactions import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('records/', views.ListRecords.as_view()),
    path('records/<int:pk>/', views.RecordDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)