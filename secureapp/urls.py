from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Include admin URLs
    path('api/auth/', include('secureauth.urls')),
]

