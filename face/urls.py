from django.urls import path
from . import views

urlpatterns = [
    path('analyze_faces', views.analyze_faces, name='analyze_faces'),
]
