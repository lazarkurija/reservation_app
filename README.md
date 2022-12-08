# Reservation App

This is a simple reservation app that allows users to see the reservations for existing rentals. It also allows to see the previous reservation history for a given rental.

## Getting Started

### Creating a virtual environment
`poetry install`

### Seeding the database
`GET /reservations/seed`

Doing this call will create a semi-random set of reservations and rentals to demo the capability of the app.

### Running the app
`poetry run python manage.py runserver`

### Demo the app
`GET /reservations/`

### Running the tests
`poetry run python manage.py test`