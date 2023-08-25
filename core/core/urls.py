
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('property_management.urls')),
    # path('api/',include('api.urls')),
    # path('api-auth/', include('rest_framework.urls')),
]
