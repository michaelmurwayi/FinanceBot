from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Accounts import views

urlpatterns = [
    path('accounts/', views.AccountsList.as_view()),
<<<<<<< HEAD
    path('accounts/<int:pk>', views.AccountDetail.as_view()),
=======
    path('accounts/<int:pk>/', views.AccountDetail.as_view()),
>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)