from django.db import models
from django.utils.timezone import now
import datetime

# Create your models here.

I = 'Inachevé'
A = 'Achevé'
ETAT = [( I,'Inachevé'),( A,'Achevé')]

EN = 'En cours'
T = 'Terminé'
ETATN = [( EN,'En cours'),( T,'Terminé')]

PP = 'Poule pondeuse'
FN = 'Poulet de chair'
TYPE = [(PP,'Poule pondeuse') , (FN, 'Poulet de chair')]

PO = 'Poulette'
PI = 'Pondeuse I'
PII = 'Pondeuse II'
PIII = 'Pondeuse III'
STOCK = [(PO,'Poulette') , (PI, 'Pondeuse I') , (PII, 'Pondeuse II') , (PIII, 'Pondeuse II')]

NaN = 'NaN'
AN = 'Anormal'
N = 'Normal'
E = 'Excellent'
OBSERVATION = [(NaN,'NaN') , (AN, 'Anormal'),(N, 'Normal'),(E,'Excellent')]

class Elevage(models.Model):
    date_debut = models.DateField(default='2021-06-20')
    type = models.CharField(max_length=17,
        choices=TYPE,
        default=PP,)
    etat = models.CharField(max_length=9,
        choices=ETAT,
        default=I,)
    nb_poulet = models.IntegerField(default = 1)



class Vaccin(models.Model):
    nom = models.CharField(max_length=20 , blank=False, default='')
    elevage = models.ForeignKey(Elevage, on_delete=models.CASCADE , default='')
    date_prescrit = models.DateField(default='2021-06-20')
    description = models.CharField(max_length=100 , blank=True , default='description not available')
    prix_unitaire = models.CharField(max_length=20 , blank=True, default='000')
    prix_total = models.IntegerField(default = 0)
    etat = models.CharField(max_length=9,
        choices=ETAT,
        default=I,)


class Prevaccin(models.Model):
    nom = models.CharField(max_length=100 , blank=False, default='')
    elevage = models.ForeignKey(Elevage, on_delete=models.CASCADE , default='')
    description = models.CharField(max_length=300 , blank=True , default='description not available')
    date_debut = models.DateField(default='2021-06-20')
    date_fin = models.DateField(default='2021-06-20')
    prix_unitaire = models.IntegerField(default = 0)
    prix_total =models.IntegerField(default = 0)
    etat = models.CharField(max_length=9, 
        choices=ETAT,
        default=I,)

class Nourriture(models.Model):
    nom = models.CharField(max_length=200 , blank=False, default='Poulette')
    date_debut = models.DateField(default='2021-06-20')
    date_fin = models.DateField(default='2021-06-20')
    elevage = models.ForeignKey(Elevage, on_delete=models.CASCADE , default='')
    quantité_journalière = models.IntegerField(default = 0)
    total_journalière = models.IntegerField(default = 0)
    quantité_total = models.IntegerField(default = 0)
    etat = models.CharField(max_length=9,
        choices=ETATN,
        default=EN,)
    details = models.CharField(max_length=200 , blank=True, default='Aucune informations')
    prix = models.IntegerField(default = 0)
    poids_estimé =models.IntegerField(default = 0)
    poids_prelevé = models.IntegerField(default = 0)
    observation = models.CharField(max_length=15,
        choices=OBSERVATION,
        default=NaN,)

class Eau(models.Model):
    date_debut = models.DateField(default='2021-06-20')
    date_fin = models.DateField(default='2021-06-20')
    elevage = models.ForeignKey(Elevage, on_delete=models.CASCADE , default='')
    quantité_journalière = models.IntegerField(default = 0)
    total_journalière = models.IntegerField(default = 0)
    quantité_total = models.IntegerField(default = 0)
    etat = models.CharField(max_length=9,
        choices=ETATN,
        default=EN,)
    prix = models.IntegerField(default = 0)


class Stock(models.Model):
    type = models.CharField(max_length=17,
        choices=STOCK,
        default=PO,)
    quantité = models.IntegerField(default = 0)


