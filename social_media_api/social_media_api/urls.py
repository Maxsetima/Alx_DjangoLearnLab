"""
URL configuration for social_media_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# social_media_api/urls.py
"""
URL configuration for the social_media_api project.

This file routes the URLs to the appropriate views for the project.
For more information on how URLs are routed in Django, visit:
https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('accounts.urls')),  # This includes all the user-related routes (register, login, etc.)
    # Add additional API routes for products, orders, logistics, payments, and reviews here
    path('api/accounts/', include('accounts.urls')),  # Redundant path, you can remove it if not needed
    path('api/posts/', include('posts.urls')),  # Add this line to include the posts app's URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
