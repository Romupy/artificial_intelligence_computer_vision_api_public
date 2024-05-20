from django.urls import path
from . import views

urlpatterns = [
    path('detect_text', views.detect_text, name='detect_text'),
    path('search_word', views.search_word, name='search_word'),
    path(
        'search_information',
        views.search_information,
        name='search_information'
    ),
]
