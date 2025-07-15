from django.urls import path
from .views import MensajeView

urlpatterns = [
    path('mensaje/', MensajeView.as_view(), name='mensaje'),
]
