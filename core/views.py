from django.shortcuts import render
from django.http import HttpResponse


# Inicio home/
#
# Historia about/
#
# Servicios services/
#
# Visítanos store/
#
# Contacto contact/
#
# Blog blog/

# Sample sample/ (esta es para páginas de prueba)

# Create your views here.
def Home(request):
    return HttpResponse('<h1>Home</h1>')


def About(request):
    return HttpResponse('<h1>About</h1>')

def Services(request):
    return HttpResponse('<h1>Services</h1>')

def Sample(request):
    return HttpResponse('<h1>Sample</h1>')
