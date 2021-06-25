from django.urls import path, include
from users.views import UserView, UserDetailView#, UserAddressDetailView

urlpatterns = [
    path('Users/', UserView.as_view()),
    path('<int:user_id>/', UserDetailView.as_view()),
    #path('<user_id>/addresses/', UserAddressDetailView.as_view())
]