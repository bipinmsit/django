from django.urls import path
from django.conf import settings
from . import views
import os

urlpatterns = [path('pdf/', views.check_projection, name='pdf')]