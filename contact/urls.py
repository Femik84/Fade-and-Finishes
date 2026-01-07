from django.urls import path
from .views import contact_view, booking_view

urlpatterns = [
    path("contact/", contact_view, name="contact"),
    path("booking/", booking_view, name="booking"),
]