from django.urls import path
from .views import contato_view, reserva_view

urlpatterns = [
    path("", contato_view, name="contato"),       # rota /contato/ com nome "contato"
    path("reserva/", reserva_view, name="reserva"),  # rota /contato/reserva/ com nome "reserva"
]

