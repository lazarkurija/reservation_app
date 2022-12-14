from django.test import TestCase

from .controller import get_reservations
from .models import Rental, Reservation

# Create your tests here.


class ReservationControllerTests(TestCase):
    def setUp(self):
        self.rental = Rental.objects.create(name="Rental 1")
        self.reservation1 = Reservation.objects.create(
            rental=self.rental, checkin="2022-01-01", checkout="2022-01-13"
        )
        self.reservation2 = Reservation.objects.create(
            rental=self.rental, checkin="2022-01-20", checkout="2022-02-10"
        )
        self.reservation3 = Reservation.objects.create(
            rental=self.rental, checkin="2022-02-20", checkout="2022-03-10"
        )

    def test_get_reservation(self):
        reservations = get_reservations()

        self.assertEqual(len(reservations), 3)

        self.assertEqual(reservations[0], self.reservation1)
        self.assertEqual(reservations[0].previous_reservation, None)

        self.assertEqual(reservations[1], self.reservation2)
        self.assertEqual(reservations[1].previous_reservation, self.reservation1.id)

        self.assertEqual(reservations[2], self.reservation3)
        self.assertEqual(reservations[2].previous_reservation, self.reservation2.id)

    def test_get_reservation_new_reservation(self):
        self.reservation4 = Reservation.objects.create(
            rental=self.rental, checkin="2022-01-14", checkout="2022-01-19"
        )
        reservations = get_reservations()

        self.assertEqual(len(reservations), 4)

        self.assertEqual(reservations[0], self.reservation1)
        self.assertEqual(reservations[0].previous_reservation, None)

        self.assertEqual(reservations[1], self.reservation2)
        self.assertEqual(reservations[1].previous_reservation, self.reservation4.id)

        self.assertEqual(reservations[2], self.reservation3)
        self.assertEqual(reservations[2].previous_reservation, self.reservation4.id)

        self.assertEqual(reservations[3], self.reservation4)
        self.assertEqual(reservations[3].previous_reservation, self.reservation1.id)

    def test_get_reservation_removed_reservation(self):
        self.reservation2.delete()
        reservations = get_reservations()

        self.assertEqual(len(reservations), 2)

        self.assertEqual(reservations[0], self.reservation1)
        self.assertEqual(reservations[0].previous_reservation, None)

        self.assertEqual(reservations[1], self.reservation3)
        self.assertEqual(reservations[1].previous_reservation, self.reservation1.id)
