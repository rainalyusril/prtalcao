from django.urls import path

from . import views
from .views import spbi_page

urlpatterns = [
    path('', views.index, name='index'),
    path('spbi/', spbi_page, name='spbi'),
]
