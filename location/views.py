from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class HelloLocationView(GenericAPIView):

    def get(self, request):
        return Response(data={"message": "Hellow location"}, status=status.HTTP_200_OK)

class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        region = self.kwargs.get("region","")
        queryset = self.queryset.filter(region__name=region)
        return queryset


class StateListAPIView(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def get_queryset(self):
        region = self.kwargs.get("region", "")
        country = self.kwargs.get("country","")
        queryset = self.queryset.filter(country__name=country,country__region__name=region)
        return queryset


class CityListAPIView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        region = self.kwargs.get("region", "")
        country = self.kwargs.get("country","")
        state = self.kwargs.get("state", "")
        queryset = self.queryset.filter(state__name=state,
                                        state__country__name=country,
                                        state__country__region__name=region)
        return queryset


class LocationListAPIView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def get_queryset(self):
        region= self.kwargs.get("region", "")
        country = self.kwargs.get("country","")
        state = self.kwargs.get("state", "")
        city = self.kwargs.get("city", "")
        queryset = self.queryset.filter(city__name=city,
                                        city__state__name=state,
                                        city__state__country__name=country,
                                        city__state__country__region__name=region)
        return queryset

