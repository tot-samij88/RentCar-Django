from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacts
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        car_name = request.POST['car_name']
        car_manager = request.POST['car_manager']
        car_id = request.POST['car_id']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['text']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(
                car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "Car alredy rented")
                return redirect("/car/"+car_id)
        contact = Contacts(cars=car_name, car_id=car_id, name=name, email=email,
                           phone=phone, message=message, user_id=user_id)
        contact.save()
        send_mail(
            'New order.',
            'Rent car .' + name + car_name + phone + message,
            'gorbanoleg8888@gmail.com',
            ['mizeravladik@gmail.com'],
            fail_silently=False
        )
        messages.success(request, "Your request submited")
        return redirect("/car/"+car_id)
