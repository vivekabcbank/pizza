from rest_framework import serializers
from .models import *


class RegionSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(RegionSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Region
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(CountrySerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Country
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(StateSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = State
        fields = "__all__"
        depth = 1


class CitySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(CitySerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = City
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(LocationSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Location
        fields = "__all__"
        depth = 2
