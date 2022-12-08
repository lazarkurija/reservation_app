from random import randint

from django.http import HttpResponse
from django.shortcuts import render

from .controller import get_reservations
from .models import Rental, Reservation

# Create your views here.


def seed_database(request):
    Rental.objects.all().delete()
    Reservation.objects.all().delete()

    for i in range(1, randint(6, 10)):
        rental = Rental.objects.create(name=f"Rental {i}")
        for j in range(1, randint(2, 25), 5):
            Reservation.objects.create(
                rental=rental, checkin=f"2021-01-{j:01}", checkout=f"2021-01-{j+randint(1, 4):01}"
            )

    return HttpResponse("Database seeded successfully!")


def reservation_view(request):
    context = {"reservations": get_reservations()}
    return render(request, "list.html", context)
