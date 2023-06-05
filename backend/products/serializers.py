from rest_framework import serializers
from .models import Bikes, Specification

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bikes
        fields = ['brand', 'bike_type', 'bike_model', 'price', 'weight', 'color']

class SpecificationSerializer(serializers.ModelSerializer):
    bikes = BikeSerializer()
    class Meta:
        model = Specification
        fields = ['bikes_id', 'frame', 'fork', 'handlebar', 'handle_tape', 'stem',\
                'seatpost', 'saddle', 'shift', 'front_derailleur',\
                'rear_derailleur', 'brake', 'brake_lever', 'cassette',\
                'chain', 'crankset', 'bottom_bracket', 'wheel',\
                'thru_axle', 'tyre', 'bikes']


# class BikeSerializer(serializers.Serializer):
#     brand =  serializers.CharField()
#     bike_type = serializers.CharField()
#     bike_model = serializers.CharField()
#     price = serializers.IntegerField()
#     weight = serializers.DecimalField(max_digits=4, decimal_places=2)
#     color = serializers.CharField()

# class SpecificationSerializer(serializers.Serializer):
#     frame = serializers.CharField()
#     fork = serializers.CharField()
#     handlebar = serializers.CharField()
#     handle_tape = serializers.CharField()
#     stem = serializers.CharField()
#     seatpost = serializers.CharField()
#     saddle = serializers.CharField()
#     shift = serializers.CharField()
#     front_derailleur = serializers.CharField()
#     rear_derailleur = serializers.CharField()
#     brake = serializers.CharField()
#     brake_lever = serializers.CharField()
#     cassette = serializers.CharField()
#     chain = serializers.CharField()
#     crankset = serializers.CharField()
#     bottom_bracket = serializers.CharField()
#     wheel = serializers.CharField()
#     thru_axle = serializers.CharField()
#     tyre = serializers.CharField()
#     bikes = BikeSerializer()


    