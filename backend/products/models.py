from django.contrib import auth
from django.db import models

class Bikes(models.Model):
    """ Based data about bike: brand, type, model, price, weight, color"""
    brand =  models.CharField(max_length=50,
                              help_text='  xx  ')
    bike_type = models.CharField(max_length=20,
                                 help_text='The type of the bike.')
    bike_model = models.CharField(max_length=20,
                                  help_text='The model of the bike.')
    price = models.IntegerField(help_text='The price of the bike.')
    weight = models.DecimalField(max_digits=4, decimal_places=2,
                                 help_text='The weight of bike.')
    color = models.CharField(max_length=20,
                             help_text='The color of the frame.')
    def __str__(self):
        return '{}'.format(self.bike_model)

class Specification(models.Model):
    """ Specification of the bikes: almost all parts"""
    frame = models.CharField(max_length=120,
                              help_text='Desctription of frame.')
    fork = models.CharField(max_length=120,
                              help_text='Material and type of lork.')
    handlebar = models.CharField(max_length=120,
                              help_text='Details of handlebar')
    handle_tape = models.CharField(max_length=120,
                              help_text='Details of handle tape.')
    stem = models.CharField(max_length=120,
                              help_text='Details of stem.')
    seatpost = models.CharField(max_length=120,
                              help_text='Details of seatpost.')
    saddle = models.CharField(max_length=120,
                              help_text='Details of saddle.')
    shift = models.CharField(max_length=120,
                              help_text='Details of shifter.')
    front_derailleur = models.CharField(max_length=120,
                              help_text='Details of front derailleur.')
    rear_derailleur = models.CharField(max_length=120,
                              help_text='Details of rear derailleur.')
    brake = models.CharField(max_length=120,
                              help_text='Details of brakes.')
    brake_lever = models.CharField(max_length=120,
                              help_text='Details of break lever.')
    cassette = models.CharField(max_length=120,
                              help_text='Details of cassette.')
    chain = models.CharField(max_length=120,
                              help_text='Details of chain.')
    crankset = models.CharField(max_length=120,
                              help_text='Details of crankset.')
    bottom_bracket = models.CharField(max_length=120,
                              help_text='Details of bottom bracket.')
    wheel = models.CharField(max_length=120,
                              help_text='Details of wheel')
    thru_axle = models.CharField(max_length=120,
                              help_text='Details of thru axle')
    tyre = models.CharField(max_length=120,
                              help_text='Details of tyre')
    bikes = models.ForeignKey(Bikes, on_delete=models.CASCADE,
                             help_text="The Book that this specification is for.")
    
  

