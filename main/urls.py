# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='home'),  # Your main view
    path('about/', views.about_redirect, name='about_redirect'), 
    path('contact/', views.contact_view, name='contact'),
]
