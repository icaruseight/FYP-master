from .views import RegisterAPI, DriverRegisterAPI, UpdateProfile, UserAPI
from knox import views as knox_views
from .views import LoginAPI, UserAPI, DriverLoginAPI
from django.urls import path

urlpatterns = [
    path('api/register/customer', RegisterAPI.as_view(), name='register'),
    path('api/register/driver', DriverRegisterAPI.as_view(), name='register'),
    path('api/user/', UserAPI.as_view(), name='login'),
    path('api/login/customer', LoginAPI.as_view(), name='login'),
    path('api/login/driver', DriverLoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/update/<username>', UpdateProfile.as_view(), name='update'),
]
