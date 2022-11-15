from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from user_data.views import *


urlpatterns = [
    path('get/', GetAPI.as_view()),
    path('register/', RegisterAPI.as_view(), name="register"),
    path('login/', LoginAPI.as_view(), name='login')
]