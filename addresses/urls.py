from django.urls import path, include
from addresses.views import AdressView

urlpatterns = [
    path('addresses/', AdressView.as_view())
]