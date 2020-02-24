
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # APIS
    path('api/v1/accounts/', include('accounts.api.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/core/', include('core.api.urls')),

    # Normal URLS
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('core/', include('core.urls', namespace='core')),
    path('admin/', admin.site.urls),
]