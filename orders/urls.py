from django.urls import path
from .views import get_menu, place_order

urlpatterns = [
    path('menu/', get_menu),
    path('order/', place_order),
]