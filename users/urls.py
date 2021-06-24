from django.urls import path, include
from users.views import UserView

urlpatterns = [
    path('Users/', UserView.as_view())
]