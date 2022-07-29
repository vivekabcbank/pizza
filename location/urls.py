from django.urls import path
from .views import *


urlpatterns = [
    # path('^region/$',RegionListAPIView.as_view(),name="region"),
    path('',RegionListAPIView.as_view(),name="region"),
    path('region/<str:region>/',CountryListAPIView.as_view(),name="country"),
    path('region/<str:region>/country/<str:country>/',StateListAPIView.as_view(),name="state"),
    path('region/<str:region>/country/<str:country>/state/<str:state>/',CityListAPIView.as_view(),name="city"),
    path('region/<str:region>/country/<str:country>/state/<str:state>/city/<str:city>/',LocationListAPIView.as_view(),name="location"),
]
