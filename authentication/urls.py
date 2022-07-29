from django.urls import path
from .views import *


urlpatterns = [
    path("",HelloAuthView.as_view(),name="hello_auth"),
    path("signup/",UserSerializer.as_view(),name="sign_up"),
]
