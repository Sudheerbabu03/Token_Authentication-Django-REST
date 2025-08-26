
from django.urls import path
from jwt_auth import views


urlpatterns = [
    path('registration/',views.TokenAuthenticationView.as_view(),name='registration'),
    path('users_data/',views.TokenAuthenticationView.as_view(),name='users-data'),
]