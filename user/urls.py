from django.urls import path

from user.views.user_registration import UserRegistrationFormView


urlpatterns = [
    path("", UserRegistrationFormView.as_view(), name="home"),
]
