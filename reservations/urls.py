from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.reservation_view, name="reservations"),
    path("seed", views.seed_database, name="seed_db"),
]
