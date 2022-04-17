from django.urls import path, include
from .views import RegistrUserView

urlpatterns = [
    path('', RegistrUserView.as_view(), name='signup'),
]
