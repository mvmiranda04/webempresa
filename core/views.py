from django.shortcuts import render
from django.http import HttpResponse


# Cambia por render
# Create your views here.
# def home(request):
#     return HttpResponse('<h1>Home</h1>')
# def about(request):
#    return HttpResponse('<h1>Historia</h1>')

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def store(request):
    return render(request, 'core/store.html')


def contact(request):
    return render(request, 'core/contact.html')


def blog(request):
    return render(request, 'core/blog.html')


def sample(request):
    return render(request, 'core/sample.html')
