from django.urls import path
from core.views import (
    ContactCreateAPIView,
)

urlpatterns = [
    path('contact/', ContactCreateAPIView.as_view(), name='contact'),
]

