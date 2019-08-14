<<<<<<< HEAD
from django.urls import path, include
=======
<<<<<<< HEAD

=======
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b
from django.urls import path
>>>>>>> fc52c12f4c0514a995a6a66629f42e40204c774f
from rest_framework.urlpatterns import format_suffix_patterns
from Accounts import views
from rest_framework.routers import DefaultRouter

<<<<<<< HEAD
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'accounts', views.AccountsViewSet)
router.register(r'owners', views.OwnersViewSet)
=======
<<<<<<< HEAD
app_name = 'Account'
>>>>>>> fc52c12f4c0514a995a6a66629f42e40204c774f

# The API URLs are now determined automatically by the router.
urlpatterns = [
<<<<<<< HEAD
    path('', include(router.urls)),
]
=======
    path('accounts/', views.AccountsList.as_view(), name= 'Account-list'),
    path('accounts/<int:pk>/', views.AccountDetail.as_view(), name= 'Account-Detail'),
    path('owners/', views.OwnersList.as_view(), name= 'ownerslist'),
    path('owners/<int:pk>/', views.OwnerDetail.as_view(), name= 'owner-Detail'),
=======
urlpatterns = [
    path('accounts/', views.AccountsList.as_view()),
<<<<<<< HEAD
    path('accounts/<int:pk>', views.AccountDetail.as_view()),
=======
    path('accounts/<int:pk>/', views.AccountDetail.as_view()),
>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b
]

urlpatterns = format_suffix_patterns(urlpatterns)
>>>>>>> fc52c12f4c0514a995a6a66629f42e40204c774f
