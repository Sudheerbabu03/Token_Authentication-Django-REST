
from django.urls import path
from jwt_auth import views


urlpatterns = [
    path('registration/',views.RegistrationView.as_view(),name='registration'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('data/<str:emp_id>/',views.UserData.as_view(),name='user_data'),
]