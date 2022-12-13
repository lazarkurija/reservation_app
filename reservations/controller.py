from .models import Rental, Reservation


def get_reservations():
    reservations = Reservation.objects.all()
    prev_reservation_id = []
    for reservation in reservations:
        prev_reservation = reservation.rental.reservation_set.filter(
            checkout__lt=reservation.checkin
        ).last()
        prev_reservation_id.append(prev_reservation.id if prev_reservation else None)

    return [
        {"reservation": r, "prev_reservation_id": p}
        for r, p in zip(reservations, prev_reservation_id)
    ]
