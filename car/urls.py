from django.urls import path

from . import views

urlpatterns = [
    path('', views.car, name="car"),
    path('<int:carslist_id>', views.carsingle, name="singlecar")
]
