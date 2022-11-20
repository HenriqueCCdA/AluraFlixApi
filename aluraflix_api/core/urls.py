from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .api.auth import register

app_name = 'core'

urlpatterns = [
    # auth
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', register, name='register'),
]
