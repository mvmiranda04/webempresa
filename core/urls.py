from django.urls import path
from .views import Home, Sample

urlpatterns = [
    path('', Home, name="home"),
    path('sample/', Sample, name="sample"),
]