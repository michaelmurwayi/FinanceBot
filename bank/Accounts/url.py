
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Accounts import views

app_name = 'Account'

urlpatterns = [
    path('accounts/', views.AccountsList.as_view(), name= 'Account-list'),
    path('accounts/<int:pk>/', views.AccountDetail.as_view(), name= 'Account-Detail'),
    path('owners/', views.OwnersList.as_view(), name= 'ownerslist'),
    path('owners/<int:pk>/', views.OwnerDetail.as_view(), name= 'owner-Detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)