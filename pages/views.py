from django.shortcuts import render
from django.core.paginator import Paginator
from car.models import CarsList
from carmanager.models import CarManager


def index(request):
    carlist = CarsList.objects.all().filter(is_published=True)
    context = {
        "carlist": carlist,
        "title": "Welcom",
        "subtitle": "This is a template for a simple marketing or informational website. It includes a large callout called ajumbotron and three supporting pieces of content. Use it as a starting point to create something more unique."
    }
    return render(request, 'pages/index.html', context)


def about(request):
    managers = CarManager.objects.all().filter(is_published=True)
    context = {
        "title": "About us",
        'managers': managers
    }
    return render(request, 'pages/about.html', context)


def services(request):
    data = {
        "title": "Services"
    }
    return render(request, 'pages/services.html', data)


def contact(request):
    data = {
        "title": "Contact"
    }
    return render(request, 'pages/contact.html', data)


def blog(request):
    data = {
        "title": "Car Articles"
    }
    return render(request, '../templates/blog/blog.html', data)


def single(request):
    data = {
        "title": "single Blog Posts Title"
    }
    return render(request, '../templates/blog/blog/single.html', data)
