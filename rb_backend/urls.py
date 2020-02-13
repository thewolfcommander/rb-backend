
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/accounts/', include('accounts.urls', namespace='accounts')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
]
