from django.db.models import F, Max, Q

from .models import Reservation


def get_reservations():
    reservations = Reservation.objects.annotate(
        previous_reservation=Max(
            "rental__reservation__id",
            filter=Q(rental__reservation__checkin__lt=F("checkin")),
        )
    ).all()

    return reservations
