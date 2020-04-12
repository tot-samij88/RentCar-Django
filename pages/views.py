from django.shortcuts import render
from django.core.paginator import Paginator
from car.models import CarsList
from carmanager.models import CarManager
from .cars_info import *


def index(request):
    carlist = CarsList.objects.all().filter(is_published=True)
    query = CarsList.objects.order_by("vendor")
    if "vendor" in request.GET:
        vendor = request.GET["vendor"]
        if vendor:
            query = query.filter(vendor__iexact=vendor)
    if "model" in request.GET:
        model = request.GET["model"]
        if model:
            query = query.filter(model__iexact=model)
    if "engine" in request.GET:
        engine = request.GET["engine"]
        if engine:
            query = query.filter(engine__iexact=engine)
    if "transmision" in request.GET:
        transmision = request.GET["transmision"]
        if transmision:
            query = query.filter(transmision__iexact=transmision)
    context = {
        "carlist": carlist,
        "title": "Welcom",
        "subtitle": "This is a template for a simple marketing or informational website. It includes a large callout called ajumbotron and three supporting pieces of content. Use it as a starting point to create something more unique.",
        "carlist": query,
        "vendor_list":vendor_list,
        "model_list":model_list,
        "engine_list":engine_list,
        "transmission_list":transmission_list
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


def search(request):
    query = CarsList.objects.order_by("vendor")
    if "vendor" in request.GET:
        vendor = request.GET["vendor"]
        if vendor:
            query = query.filter(vendor__iexact=vendor)
    if "model" in request.GET:
        model = request.GET["model"]
        if model:
            query = query.filter(model__iexact=model)
    if "engine" in request.GET:
        engine = request.GET["engine"]
        if engine:
            query = query.filter(engine__iexact=engine)
    if "transmision" in request.GET:
        transmision = request.GET["transmision"]
        if transmision:
            query = query.filter(transmision__iexact=transmision)
    context = {
        "carlist": query,
        "vendor_list":vendor_list,
        "model_list":model_list,
        "engine_list":engine_list,
        "transmission_list":transmission_list,
        
    }
    return render(request, 'pages/search.html', context)
