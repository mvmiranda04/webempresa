from django.urls import path
from .views import home, sample, services, store, contact, blog, about

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('services/', services, name="services"),
    path('store/', store, name="store"),
    path('contact/', contact, name="contact"),
    path('blog/', blog, name="blog"),
    path('sample/', sample, name="sample"),
]