from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import CarsList
from carmanager.models import CarManager


def car(request):
    carlist = CarsList.objects.all().filter(is_published=True)
    paginator = Paginator(carlist, 3)
    page = request.GET.get("page")
    paged_carlist = paginator.get_page(page)

    context = {
        "carlist": paged_carlist,
        "title": "Car listining"
    }

    return render(request, 'car/car.html', context)


def carsingle(request, carslist_id):
    car = get_object_or_404(CarsList, pk=carslist_id)
    managers = get_object_or_404(CarManager, name=car.carmanager)
    context = {
        "car": car,
        "title": "Your choice",
        'managers': managers
    }
    return render(request, 'car/singlecar.html', context)
