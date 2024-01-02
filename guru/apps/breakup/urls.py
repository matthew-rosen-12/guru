"""
URL configuration for breakup app.
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('people', views.PersonViewSet.as_view({'get': 'list'}), name='people'),
]
