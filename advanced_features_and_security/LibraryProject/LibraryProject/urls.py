# LibraryProject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('relationship_app.urls')),  # Include the app's authentication URLs
]

