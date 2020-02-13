from django.urls import path
from .views import HelloAPIView

app_name = 'accounts'

urlpatterns = [
    path('', HelloAPIView.as_view(), name='hello'),
]