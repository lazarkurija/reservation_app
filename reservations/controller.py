from django.db.models import OuterRef, Subquery

from .models import Reservation


def get_reservations():
    reservations = Reservation.objects.annotate(
        previous_reservation=Subquery(
            Reservation.objects.filter(
                rental=OuterRef("rental"),
                checkout__lt=OuterRef("checkin"),
            )
            .order_by("-checkin")
            .values("id")
        )
    ).all()

    return reservations
