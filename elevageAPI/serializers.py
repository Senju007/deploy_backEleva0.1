from rest_framework import serializers
from elevageAPI.models import Elevage , Vaccin , Nourriture , Prevaccin , Eau , Stock


class ElevageSerializer(serializers.ModelSerializer):

    class  Meta:
        model = Elevage
        fields =('id','date_debut','nb_poulet','type','etat')

class VaccinSerializer(serializers.ModelSerializer):
    
    class  Meta:
        model = Vaccin
        fields =('id','nom','elevage','date_prescrit','description','etat','prix_unitaire','prix_total')

class NourritureSerializer(serializers.ModelSerializer):
    
    class  Meta:
        model = Nourriture
        fields =('id','nom','date_debut','date_fin','elevage','quantité_journalière','quantité_total','total_journalière','etat','prix','poids_estimé','poids_prelevé','details','observation')

class PrevaccinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prevaccin
        fields =('id','elevage','nom','description','date_debut','date_fin','prix_unitaire','prix_total','etat')

class EauSerializer(serializers.ModelSerializer):

    class Meta:
        model = Eau 
        fields = ('id','elevage','quantité_journalière','quantité_total','total_journalière','date_debut','date_fin','prix','etat')

class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stock 
        fields = ('id','quantité','type')