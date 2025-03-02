# LibraryProject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('relationship_app.urls')),  # Include the app's authentication URLs
]

urlpatterns = [
    path('example/', views.example_view, name='example_form'),
]