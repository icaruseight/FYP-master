from django.db import models

# Create your models here.

TYPE_CHOICES = (
    ('Document','DOCUMENT'),
    ('parcel', 'PARCEL'),
)

WEIGHT_CHOICE = (
    ('Less than 1 kg', '<1KG'),
    ('1-4kg', '1-4 KG'),
    ('5-9 kg','5-9 KG'),
    ('10-19 kg','10-19 KG',),
    ('20-49 kg','20-49 KG'),
    ('50-99 kg', '50-99 KG'),
    ('100+ kg','100+ KG'),
)


SIZE_CHOICE = (
    ('Less than 1 m', '<1 m'),
    ('1-4 m', '1-4 M'),
    ('4-9 m','4-9 M'), 
    ('10-15 m', '10-15 M'),
)


class Pricing(models.Model):
    typeOf = models.CharField(max_length=100, choices=TYPE_CHOICES, default='document')
    weight = models.CharField(max_length=100, choices=WEIGHT_CHOICE, default='less than 1 kg')
    size = models.CharField(max_length=100, choices=SIZE_CHOICE, default='less than 1 m')
    price = models.CharField(max_length=100)