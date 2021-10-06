# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status , viewsets
from elevageAPI.models import Elevage , Vaccin , Nourriture , Prevaccin , Eau , Stock
from elevageAPI.serializers import ElevageSerializer , VaccinSerializer , NourritureSerializer , PrevaccinSerializer , EauSerializer , StockSerializer
from rest_framework.decorators import api_view , permission_classes
from django.db.models import Count , F , Value , Sum
from experta import *
import datetime
from datetime import timedelta ,  date
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

# Create your views here.

from user_management.serializers import UserSerializer
from django.contrib.auth.models import User


class ElevageViewSet(viewsets.ModelViewSet):

    queryset = Elevage.objects.all()
    serializer_class = ElevageSerializer
    #permission_classes = (IsAuthenticated , )

@api_view(['GET'])
def user(request):

    if request.method == 'GET':
        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return JsonResponse(user_data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
#@permission_classes([IsAuthenticated])
def elevage_list(request):
  
   if request.method == 'GET':
        elevage = Elevage.objects.all()
        elevage_serializer = ElevageSerializer(elevage, many=True)
        
        return JsonResponse(elevage_serializer.data, safe=False)
        

   elif request.method == 'POST':
        elevage_data = JSONParser().parse(request)
        elevage_serializer = ElevageSerializer(data=elevage_data)
        if elevage_serializer.is_valid():
            elevage_serializer.save()
            elevage_data = json.dumps(elevage_data)
            elevage_data_json = json.loads(elevage_data)
            class initialisation(KnowledgeEngine):

                @Rule(Fact(type='Poule pondeuse'))
                def premier_vaccin_pdc(self):

                     last_elevage = Elevage.objects.latest('id')
                     elevage_last = ElevageSerializer(last_elevage, many=False)
                     last = elevage_last.data
                     last_data = json.dumps(last)
                     last_data_json = json.loads(last_data)

                     stock = Stock.objects.get(id=1)
                     stock_serializer = StockSerializer(stock, many=False)
                     lastst = stock_serializer.data
                     last_dataS = json.dumps(lastst)
                     last_data_jsonS = json.loads(last_dataS)
                     stock_val = last_data_jsonS["quantité"]

                     last_id = (last_data_json["id"])
                     last_date = last_data_json["date_debut"]


                     date_init = datetime.datetime.strptime(last_date, "%Y-%m-%d")

                     date_initN = date_init.strftime("%Y-%m-%d")
                     date_fin = date_init + timedelta(days=13)
                     date_fin_format = date_fin.strftime("%Y-%m-%d")
                     nb_poulet = last_data_json["nb_poulet"]
                     quantite_total = 52 * 14 * nb_poulet
                     res_stock = stock_val - quantite_total
                     total_journalière = 52 * 1 * nb_poulet
                     total_journalière_eau = 115 * nb_poulet
                     quantite_total_eau = 115 * nb_poulet * 14
                     date_fin_antistress = date_init + timedelta(days=2)
                     date_fin_antistress_format = date_fin_antistress.strftime("%Y-%m-%d")

                # Initialisation du premier vaccin
                     
                     
                     prevaccin_data = {'nom': 'ANTI-STRESS' , 'elevage' : last_id , 'description': 'prise d''anti-stress  pendant les 3 premier jours ','date_debut' : ''+date_initN+'' , 'date_fin': ''+date_fin_antistress_format+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                     prevaccin_data1 = {'nom': 'VITAMINE 1' , 'elevage' : last_id , 'description': 'Prise de vitamine sans medicaments Ex: VITAFLASH une(1) cuillere a soupe pour 5 litres d''eau ','date_debut' : ''+date_initN+'' , 'date_fin': ''+date_initN+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                     nourriture_data = { 'elevage' : last_id ,'date_debut' : ''+date_initN+'','date_fin': ''+date_fin_format+''  , 'quantité_journalière' : 52 , 'total_journalière': total_journalière , 'quantité_total': quantite_total , 'etat' : 'En cours' , 'prix': 0 , 'details': 'Aucune details' , 'poids_estimé': 650, 'poids_prelevé': 0 }
                     eau_data = {'elevage' : last_id ,'date_debut' : ''+date_initN+'','date_fin': ''+date_fin_format+''  , 'quantité_journalière' : 115 , 'total_journalière': total_journalière_eau , 'quantité_total': quantite_total_eau , 'etat' : 'En cours' , 'prix': 0 }
                     
                     nourriture_serializer = NourritureSerializer(data=nourriture_data)
                     prevaccin_serializer = PrevaccinSerializer(data=prevaccin_data)
                     prevaccin_serializer1 = PrevaccinSerializer(data=prevaccin_data1)
                     eau_serializer =  EauSerializer(data=eau_data)

                     if prevaccin_serializer.is_valid()&nourriture_serializer.is_valid()&prevaccin_serializer1.is_valid()&eau_serializer.is_valid():
                        prevaccin_serializer1.save()
                        prevaccin_serializer.save()
                        nourriture_serializer.save()
                        eau_serializer.save()
                        Stock.objects.filter(pk=1).update(quantité = res_stock)
                        return JsonResponse(elevage_serializer.data, status=status.HTTP_201_CREATED)
                     else:
                         print("serializer invalid")
                     return JsonResponse(elevage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            


                @Rule(Fact(type='Poulet de chair'))
                def premier_vaccin_pp(self):

                     

                     last_elevage = Elevage.objects.latest('id')
                     elevage_last = ElevageSerializer(last_elevage, many=False)
                     last = elevage_last.data
                     last_data = json.dumps(last)
                     last_data_json = json.loads(last_data)

                     last_id = (last_data_json["id"])
                     last_date = last_data_json["date_debut"]

                     date_init = datetime.datetime.strptime(last_date, "%Y-%m-%d")
                     date_days = date_init + timedelta(days=8)
                     date_prescrit = date_days.strftime("%Y-%m-%d")

                     date_initN = date_init.strftime("%Y-%m-%d")
                     date_fin = date_init + timedelta(days=6)
                     date_fin_format = date_fin.strftime("%Y-%m-%d")
                     nb_poulet = last_data_json["nb_poulet"]
                     print(nb_poulet)
                     quantite_total = 30 * 7 * nb_poulet
            # Initialisation

                     vaccin_data = {'nom': 'GUMBORO', 'elevage': last_id , 'date_prescrit' :''+date_prescrit+'', 'description': 'premier vaccin' ,'prix_unitaire ': 0 , 'prix_total': 0}
                     nourriture_data = { 'elevage' : last_id ,'date_debut' : ''+date_initN+'','date_fin': ''+date_fin_format+''  ,'quantité_journalière' : '30' ,'quantité_total': quantite_total , 'etat' : 'En cours' , 'prix': 0 , 'details': 'Aucune details' , 'poids_estimé':'120g à 150g','poids_relevé': 0 }
                     vaccin_serializer = VaccinSerializer(data=vaccin_data)
                     nourriture_serializer = NourritureSerializer(data=nourriture_data)
                     if vaccin_serializer.is_valid()&nourriture_serializer.is_valid():
                        vaccin_serializer.save()
                        nourriture_serializer.save()
                        return JsonResponse(elevage_serializer.data, status=status.HTTP_201_CREATED)
                     return JsonResponse(elevage_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

            engine = initialisation()
            engine.reset()
            engine.declare(Fact(type = elevage_data_json["type"]))
            engine.run()
            return JsonResponse(elevage_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(elevage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def elevage_nombre(request):
    if request.method == 'GET':

        nombre = Elevage.objects.count()
        return JsonResponse(nombre , safe=False)
# stock
@api_view(['GET', 'POST', 'DELETE'])
def poulette(request):
    if request.method == 'GET':

        stock = Stock.objects.get(id=1)
        stock_serializer = StockSerializer(stock, many=False)
        
        return JsonResponse(stock_serializer.data, safe=False)

api_view(['GET', 'POST', 'DELETE'])
def pondeuseI(request):
    if request.method == 'GET':

        stock = Stock.objects.get(id=2)
        stock_serializer = StockSerializer(stock, many=False)
        
        return JsonResponse(stock_serializer.data, safe=False)

api_view(['GET', 'POST', 'DELETE'])
def pondeuseII(request):
    if request.method == 'GET':

        stock = Stock.objects.get(id=3)
        stock_serializer = StockSerializer(stock, many=False)
        
        return JsonResponse(stock_serializer.data, safe=False)

api_view(['GET', 'POST', 'DELETE'])
def pondeuseIII(request):
    if request.method == 'GET':

        stock = Stock.objects.get(id=4)
        stock_serializer = StockSerializer(stock, many=False)
        
        return JsonResponse(stock_serializer.data, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def stock(request):
    if request.method == 'GET':

        stock = Stock.objects.all()
        stock_serializer = StockSerializer(stock, many=True)
        
        return JsonResponse(stock_serializer.data, safe=False)

    elif request.method == 'POST':
        stock_data = JSONParser().parse(request)
        stock_serializer = StockSerializer(data=elevage_data)
        if stock_serializer.is_valid():
            stock_serializer.save()
            return JsonResponse(stock_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(stock_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST', 'DELETE'])
def elevage_last(request):
    if request.method == 'GET':
    
        elevage = Elevage.objects.latest('id')

        elevage_serializer = ElevageSerializer(elevage, many=False)
        return JsonResponse(elevage_serializer.data, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
def elevage_detail(request, pk):

    try:
        elevage = Elevage.objects.get(pk=pk)
    except Elevage.DoesNotExist:
        return JsonResponse({'message': 'The Elevage does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        elevage_serializer = ElevageSerializer(elevage)
        return JsonResponse(elevage_serializer.data)


    elif request.method == 'DELETE':
        elevage.delete()
        return JsonResponse({'message': 'Elevage was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


    elif request.method == 'PUT':
        elevage_data = JSONParser().parse(request)
        elevage_serializer = ElevageSerializer(elevage, data=elevage_data)
        if elevage_serializer.is_valid():
            elevage_serializer.save()
            return JsonResponse(elevage_serializer.data)
        return JsonResponse(elevage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def elevage_nourriture(request,pk):
   if request.method == 'GET':
    
        nourriture = Nourriture.objects.filter(elevage=pk)

        nourriture_serializer = NourritureSerializer(nourriture, many=True)
        return JsonResponse(nourriture_serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def elevage_nourriture_total(request,pk):
   if request.method == 'GET':
    
        nourritureTotal = Nourriture.objects.filter(elevage=pk).aggregate(Sum('quantité_total'))

        return JsonResponse(nourritureTotal , safe=False)

############################################################################

@api_view(['GET', 'PUT', 'DELETE'])
def notification_nourriture(request):
   if request.method == 'GET':

        date_now = date.today()
        date_av = date_now + timedelta(days=7)
        date_av = date_av.strftime("%Y-%m-%d")

        nourriture_fin = Nourriture.objects.filter(date_fin__gte=date_now, date_fin__lte=date_av)
        

        nourriture_serializer = NourritureSerializer(nourriture_fin, many=True)
        return JsonResponse(nourriture_serializer.data, safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def notification_soins(request):
   if request.method == 'GET':
       
        date_now = date.today()
        date_av = date_now + timedelta(days=7)
        date_av = date_av.strftime("%Y-%m-%d")

        prevaccin_fin = Prevaccin.objects.filter(date_debut__gte=date_now, date_debut__lte=date_av)
        

        prevaccin_serializer = PrevaccinSerializer(prevaccin_fin, many=True)
        return JsonResponse(prevaccin_serializer.data, safe=False)


# vaccin

@api_view(['GET', 'POST', 'DELETE'])
def vaccin_list(request):
   if request.method == 'GET':

        vaccin = Vaccin.objects.all()

        vaccin_serializer = VaccinSerializer(vaccin, many=True)
        return JsonResponse(vaccin_serializer.data, safe=False)

   elif request.method == 'POST':
        vaccin_data = JSONParser().parse(request)
        vaccin_serializer = VaccinSerializer(data=vaccin_data)
        if vaccin_serializer.is_valid():
            vaccin_serializer.save()
            return JsonResponse(vaccin_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(vaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST', 'PUT', 'DELETE'])
def vaccin_detail(request, pk):

    try:
        vaccin = Vaccin.objects.get(pk=pk)
    except Vaccin.DoesNotExist:
        return JsonResponse({'message': 'The Elevage does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vaccin_serializer = VaccinSerializer(vaccin)
        return JsonResponse(vaccin_serializer.data)


    elif request.method == 'DELETE':
        vaccin.delete()
        return JsonResponse({'message': 'Elevage was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


    elif request.method == 'PUT':
        vaccin_data = JSONParser().parse(request)
        vaccin_serializer = VaccinSerializer(vaccin, data=vaccin_data)
        if vaccin_serializer.is_valid():
            vaccin_serializer.save()
            vaccin_data = json.dumps(vaccin_data)
            vaccin_data_json = json.loads(vaccin_data)



            last_elevage = Elevage.objects.get(pk=vaccin_data_json["elevage"])
            elevage_last = ElevageSerializer(last_elevage, many=False)
            last = elevage_last.data
            last_data = json.dumps(last)
            last_data_json = json.loads(last_data)


            class vaccinKnowledge(KnowledgeEngine):
            
                @Rule(Fact(etat='Achevé'),Fact(nom='ANTI-STRESS'),Fact(type='Poule pondeuse'))
                def vaccin(self):

                    date = vaccin_data_json["date_prescrit"]
                    date_init = datetime.datetime.strptime(date, "%Y-%m-%d")
                    date_days = date_init + timedelta(days=14)
                    date_prescrit = date_days.strftime("%Y-%m-%d")

                    Vaccin.objects.create(nom="ODIKANKANA",elevage= last_elevage,date_prescrit=date_prescrit,description="deuxieme vaccin",prix= 0)
                
                @Rule(Fact(etat='Achevé'),Fact(nom='GUMBORO'),Fact(type='Poulet de chair'))
                def vaccin(self):

                    date = vaccin_data_json["date_prescrit"]
                    date_init = datetime.datetime.strptime(date, "%Y-%m-%d")
                    date_days = date_init + timedelta(days=7)
                    date_prescrit = date_days.strftime("%Y-%m-%d")

                    vaccin_data = {'nom': 'GUMBORO(Rappel)', 'elevage': vaccin_data_json["elevage"] , 'date_prescrit' :''+date_prescrit+'', 'description': 'rappelle gumboro ' , 'prix_unitaire': 0 }
                    print(vaccin_data)

                    Vaccin.objects.create(nom="GUMBORO(Rappel)",elevage = last_elevage,date_prescrit=date_prescrit,description="deuxieme vaccin",prix= 0)
            
            engine = vaccinKnowledge()
            engine.reset()
            engine.declare(Fact(etat = vaccin_data_json["etat"]),Fact(nom=vaccin_data_json["nom"]),Fact(type=last_data_json["type"]))
            engine.run()
            return JsonResponse(vaccin_serializer.data)
        return JsonResponse(vaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Nourriture 


@api_view(['GET', 'POST', 'DELETE'])
def nourriture_list(request):
   if request.method == 'GET':

        nourriture = Nourriture.objects.all()

        nourriture_serializer = NourritureSerializer(nourriture, many=True)
        return JsonResponse(nourriture_serializer.data, safe=False)

   elif request.method == 'POST':
        nourriture_data = JSONParser().parse(request)
        nourriture_serializer = NourritureSerializer(data=nourriture_data)
        if nourriture_serializer.is_valid():
            nourriture_serializer.save()
            return JsonResponse(nourriture_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(nourriture_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def nourriture_detail(request, pk):

    try:
        nourriture = Nourriture.objects.get(pk=pk)
    except Nourriture.DoesNotExist:
        return JsonResponse({'message': 'The Nourriture does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        nourriture_serializer = NourritureSerializer(nourriture)
        return JsonResponse(nourriture_serializer.data)


    elif request.method == 'DELETE':
        nourriture.delete()
        return JsonResponse({'message': 'Nourriture was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


    elif request.method == 'PUT':
        nourriture_data = JSONParser().parse(request)
        nourriture_serializer = NourritureSerializer(nourriture, data=nourriture_data)
        if nourriture_serializer.is_valid():
            nourriture_serializer.save()

            



            nourriture = Nourriture.objects.get(pk=pk)
            nourriture =  NourritureSerializer(nourriture , many = False)
            nourriture = nourriture.data
            nourriture_data = json.dumps(nourriture)
            nourriture_data_json = json.loads(nourriture_data)

            nombre = Nourriture.objects.filter(elevage_id=nourriture_data_json["elevage"]).count()

            poids_prelevé = nourriture_data_json["poids_prelevé"]
            poids_estimé = nourriture_data_json["poids_estimé"]
            print(poids_prelevé)
            print(poids_estimé)
            if (poids_prelevé > poids_estimé) :
                Nourriture.objects.filter(pk=pk).update(observation = "Excellent")
            if (poids_prelevé < poids_estimé):
                Nourriture.objects.filter(pk=pk).update(observation = "Anormal")
            if (poids_prelevé == poids_estimé):
                Nourriture.objects.filter(pk=pk).update(observation = "Normal")




            last_elevage = Elevage.objects.get(pk=nourriture_data_json["elevage"])
            elevage_last = ElevageSerializer(last_elevage, many=False)
            last = elevage_last.data
            last_data = json.dumps(last)
            last_data_json = json.loads(last_data)
      
            stock = Stock.objects.get(id=1)
            stock_serializer = StockSerializer(stock, many=False)
            lastst = stock_serializer.data
            last_dataS = json.dumps(lastst)
            last_data_jsonS = json.loads(last_dataS)
            stock_val = last_data_jsonS["quantité"]

            class ElevageNourriture(KnowledgeEngine):

                @Rule(Fact(etat='Terminé'),Fact(quantité_journalière = 52),Fact(type='Poule pondeuse'),Fact(nom='Poulette'),Fact(nombre = 1))
                def nourriture(self):
                    date_debut = nourriture_data_json["date_fin"]
                    dateF_debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d")
                    dateFD_days = dateF_debut  + timedelta(days=1)
                    dateFF_days  = dateFD_days + timedelta(days=14)
                    n_debut = dateFD_days.strftime("%Y-%m-%d")
                    n_fin =  dateFF_days.strftime("%Y-%m-%d")

                    nb_poulet = last_data_json["nb_poulet"]
                    quantite_total = 60 * 14 * nb_poulet
                    res_stock = stock_val - quantite_total
                    total_journalièreC = 60 * 1 * nb_poulet
                    quantite_total_eau = 120 * 17 * nb_poulet
                    total_journalière_eau = 120 * nb_poulet

                    Nourriture.objects.create(elevage=last_elevage , nom='Poulette' ,date_debut = n_debut , date_fin = n_fin , quantité_journalière= 60 , total_journalière = total_journalièreC , quantité_total = quantite_total , poids_estimé = 800 )
                    
                    Eau.objects.create(elevage=last_elevage ,date_debut = n_debut , date_fin = n_fin , quantité_journalière= 120 , total_journalière = total_journalière_eau, quantité_total = quantite_total_eau)
                    Stock.objects.filter(pk=1).update(quantité = res_stock)

                @Rule(Fact(etat='Terminé'),Fact(quantité_journalière=60),Fact(type='Poule pondeuse'),Fact(nom='Poulette'),Fact(nombre = 2))
                def nourriture1(self):

                    date_debut = nourriture_data_json["date_fin"]
                    dateF_debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d")
                    dateFD_days = dateF_debut  + timedelta(days=1)
                    dateFF_days  = dateFD_days + timedelta(days=14)
                    n_debut = dateFD_days.strftime("%Y-%m-%d")
                    n_fin =  dateFF_days.strftime("%Y-%m-%d")

                    nb_poulet = last_data_json["nb_poulet"]
                    quantite_total = 70 * 14 * nb_poulet
                    res_stock = stock_val - quantite_total
                    total_journalièreC = 70 * 1 * nb_poulet

                   
                    Nourriture.objects.create(elevage=last_elevage , nom='Poulette' ,date_debut = n_debut , date_fin = n_fin , quantité_journalière= 70 , total_journalière = total_journalièreC , quantité_total = quantite_total , poids_estimé = 900 )
                    Stock.objects.filter(pk=1).update(quantité = res_stock)

                @Rule(Fact(etat='Terminé'),Fact(quantité_journalière=70),Fact(type='Poule pondeuse'),Fact(nom='Poulette'),Fact(nombre = 3))
                def nourriture2(self):

                    date_debut = nourriture_data_json["date_fin"]
                    dateF_debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d")
                    dateFD_days = dateF_debut  + timedelta(days=1)
                    dateFF_days  = dateFD_days + timedelta(days=14)
                    n_debut = dateFD_days.strftime("%Y-%m-%d")
                    n_fin =  dateFF_days.strftime("%Y-%m-%d")

                    nb_poulet = last_data_json["nb_poulet"]
                    quantite_total = 78 * 14 * nb_poulet
                    res_stock = stock_val - quantite_total
                    total_journalièreC = 78 * 1 * nb_poulet

                    Nourriture.objects.create(elevage=last_elevage,nom='Poulette' ,date_debut = n_debut , date_fin = n_fin , quantité_journalière= 78 , total_journalière = total_journalièreC , quantité_total = quantite_total , poids_estimé = 1000 )
                    Stock.objects.filter(pk=1).update(quantité = res_stock)

                @Rule(Fact(etat='Terminé'),Fact(quantité_journalière=78),Fact(type='Poule pondeuse'),Fact(nom='Poulette'),Fact(nombre = 4))
                def nourriture3(self):

                    date_debut = nourriture_data_json["date_fin"]
                    dateF_debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d")
                    dateFD_days = dateF_debut  + timedelta(days=1)
                    dateFF_days  = dateFD_days + timedelta(days=14)
                    n_debut = dateFD_days.strftime("%Y-%m-%d")
                    n_fin =  dateFF_days.strftime("%Y-%m-%d")

                    nb_poulet = last_data_json["nb_poulet"]
                    quantite_total = 80 * 14 * nb_poulet
                    res_stock = stock_val - quantite_total
                    total_journalièreC = 80 * 1 * nb_poulet

                    Nourriture.objects.create(elevage=last_elevage,nom='Poulette' ,date_debut = n_debut , date_fin = n_fin , quantité_journalière= 80 , total_journalière = total_journalièreC , quantité_total = quantite_total , poids_estimé = 1200  )
                    Stock.objects.filter(pk=1).update(quantité = res_stock)

                @Rule(Fact(etat='Terminé'),Fact(quantité_journalière=80),Fact(type='Poule pondeuse'),Fact(nom='Poulette'),Fact(nombre = 5))
                def nourriture4(self):

                    date_debut = nourriture_data_json["date_fin"]
                    dateF_debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d")
                    dateFD_days = dateF_debut  + timedelta(days=1)
                    dateFF_days  = dateFD_days + timedelta(days=42)
                    n_debut = dateFD_days.strftime("%Y-%m-%d")
                    n_fin =  dateFF_days.strftime("%Y-%m-%d")

                    nb_poulet = last_data_json["nb_poulet"]
                    quantite_total = 90 * 42 * nb_poulet
                    res_stock = stock_val - quantite_total
                    total_journalièreC = 90 * 1 * nb_poulet

                    Nourriture.objects.create(elevage=last_elevage , nom= 'Pondeuse I' ,date_debut = n_debut , date_fin = n_fin , quantité_journalière= 90 , total_journalière = total_journalièreC , quantité_total = quantite_total , poids_estimé = 1450  )
                    Stock.objects.filter(pk=2).update(quantité = res_stock)

                @Rule(Fact(etat='Terminé'),Fact(quantité_journalière=90),Fact(type='Poule pondeuse'),Fact(nom='Pondeuse I'),Fact(nombre = 6))
                def nourriture5(self):

                    date_debut = nourriture_data_json["date_fin"]
                    dateF_debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d")
                    dateFD_days = dateF_debut  + timedelta(days=1)
                    dateFF_days  = dateFD_days + timedelta(days=42)
                    n_debut = dateFD_days.strftime("%Y-%m-%d")
                    n_fin =  dateFF_days.strftime("%Y-%m-%d")

                    nb_poulet = last_data_json["nb_poulet"]
                    quantite_total = 120 * 42 * nb_poulet
                    res_stock = stock_val - quantite_total
                    total_journalièreC = 120 * 1 * nb_poulet

                    Nourriture.objects.create(elevage=last_elevage , nom='Pondeuse I' ,date_debut = n_debut , date_fin = n_fin , quantité_journalière= 120 , total_journalière = total_journalièreC , quantité_total = quantite_total , poids_estimé = 1600  )
                    Stock.objects.filter(pk=2).update(quantité = res_stock)

                @Rule(Fact(etat='Terminé'),Fact(quantité_journalière=120),Fact(type='Poule pondeuse'),Fact(nom='Pondeuse I'),Fact(nombre = 7))
                def nourriture6(self):

                    date_debut = nourriture_data_json["date_fin"]
                    dateF_debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d")
                    dateFD_days = dateF_debut  + timedelta(days=1)
                    dateFF_days  = dateFD_days + timedelta(days=42)
                    n_debut = dateFD_days.strftime("%Y-%m-%d")
                    n_fin =  dateFF_days.strftime("%Y-%m-%d")

                    nb_poulet = last_data_json["nb_poulet"]
                    quantite_total = 130 * 42 * nb_poulet
                    res_stock = stock_val - quantite_total
                    total_journalièreC = 130 * 1 * nb_poulet

                    Nourriture.objects.create(elevage=last_elevage ,nom = 'Pondeuse I',date_debut = n_debut , date_fin = n_fin , quantité_journalière= 130 , total_journalière = total_journalièreC , quantité_total = quantite_total , poids_estimé = 1850  )
                    Stock.objects.filter(pk=2).update(quantité = res_stock)

                @Rule(Fact(etat='Terminé'),Fact(quantité_journalière=130),Fact(type='Poule pondeuse'),Fact(nom='Pondeuse I'),Fact(nombre = 8))
                def nourriture7(self):

                    date_debut = nourriture_data_json["date_fin"]
                    dateF_debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d")
                    dateFD_days = dateF_debut  + timedelta(days=1)
                    dateFF_days  = dateFD_days + timedelta(days=70)
                    n_debut = dateFD_days.strftime("%Y-%m-%d")
                    n_fin =  dateFF_days.strftime("%Y-%m-%d")

                    nb_poulet = last_data_json["nb_poulet"]
                    quantite_total = 133 * 70 * nb_poulet
                    res_stock = stock_val - quantite_total
                    total_journalièreC = 133 * 1 * nb_poulet

                    Nourriture.objects.create(elevage=last_elevage ,nom='Pondeuse I',date_debut = n_debut , date_fin = n_fin , quantité_journalière= 133 , total_journalière = total_journalièreC , quantité_total = quantite_total , poids_estimé = 1880  )
                    Stock.objects.filter(pk=2).update(quantité = res_stock)

                @Rule(Fact(etat='Terminé'),Fact(quantité_journalière=133),Fact(type='Poule pondeuse'),Fact(nom='Pondeuse I'),Fact(nombre = 9))
                def nourriture8(self):

                    date_debut = nourriture_data_json["date_fin"]
                    dateF_debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d")
                    dateFD_days = dateF_debut  + timedelta(days=1)
                    dateFF_days  = dateFD_days + timedelta(days=182)
                    n_debut = dateFD_days.strftime("%Y-%m-%d")
                    n_fin =  dateFF_days.strftime("%Y-%m-%d")

                    nb_poulet = last_data_json["nb_poulet"]
                    quantite_total = 134 * 182 * nb_poulet
                    res_stock = stock_val - quantite_total
                    total_journalièreC = 134 * 1 * nb_poulet
                    Nourriture.objects.create(elevage=last_elevage ,nom = 'Pondeuse II',date_debut = n_debut , date_fin = n_fin , quantité_journalière= 134 , total_journalière = total_journalièreC , quantité_total = quantite_total , poids_estimé = 1900  )
                    Stock.objects.filter(pk=3).update(quantité = res_stock)

                @Rule(Fact(etat='Terminé'),Fact(quantité_journalière=134),Fact(type='Poule pondeuse'),Fact(nom='Pondeuse II'),Fact(nombre = 10))
                def nourriture9(self):

                    date_debut = nourriture_data_json["date_fin"]
                    dateF_debut = datetime.datetime.strptime(date_debut, "%Y-%m-%d")
                    dateFD_days = dateF_debut  + timedelta(days=1)
                    dateFF_days  = dateFD_days + timedelta(days=182)
                    n_debut = dateFD_days.strftime("%Y-%m-%d")
                    n_fin =  dateFF_days.strftime("%Y-%m-%d")
                    nb_poulet = last_data_json["nb_poulet"]
                    quantite_total = 135 * 182 * nb_poulet
                    res_stock = stock_val - quantite_total
                    total_journalièreC = 135 * 1 * nb_poulet

                    Nourriture.objects.create(elevage=last_elevage, nom='Pondeuse II' ,date_debut = n_debut , date_fin = n_fin , quantité_journalière= 135 , total_journalière = total_journalièreC , quantité_total = quantite_total , poids_estimé = 1920  )
                    Stock.objects.filter(pk=3).update(quantité = res_stock)

            engine = ElevageNourriture()
            engine.reset()
            engine.declare(Fact(etat = nourriture_data_json["etat"]),Fact(quantité_journalière = nourriture_data_json["quantité_journalière"]),Fact(type = last_data_json["type"]),Fact(nom = nourriture_data_json["nom"]),Fact(nombre = nombre))
            engine.run()
            return JsonResponse(nourriture_serializer.data)
        return JsonResponse(nourriture_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#prevaccin
@api_view(['GET', 'POST', 'DELETE'])
def prevaccin(request):
   if request.method == 'GET':

        prevaccin = Prevaccin.objects.all()

        prevaccin_serializer = PrevaccinSerializer(prevaccin, many=True)
        return JsonResponse(prevaccin_serializer.data, safe=False)

   elif request.method == 'POST':
        prevaccin_data = JSONParser().parse(request)
        prevaccin_serializer = PrevaccinSerializer(data=prevaccin_data)
        if prevaccin_serializer.is_valid():
            prevaccin_serializer.save()
            return JsonResponse(prevaccin_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(prevaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST', 'PUT', 'DELETE'])
def prevaccin_detail(request, pk):

    try:
        prevaccin = Prevaccin.objects.get(pk=pk)
    except Prevaccin.DoesNotExist:
        return JsonResponse({'message': 'The Prevaccin does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        prevaccin_serializer = PrevaccinSerializer(prevaccin)
        return JsonResponse(prevaccin_serializer.data)


    elif request.method == 'DELETE':
        prevaccin.delete()
        return JsonResponse({'message': 'Prevaccin was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


    elif request.method == 'PUT':
        prevaccin_data = JSONParser().parse(request)
        prevaccin_serializer = PrevaccinSerializer(prevaccin, data=prevaccin_data)
        if prevaccin_serializer.is_valid():
            prevaccin_serializer.save()

            prevaccin = Prevaccin.objects.get(pk=pk)
            prevaccin =  PrevaccinSerializer(prevaccin , many = False)
            prevaccin = prevaccin.data
            prevaccin_data = json.dumps(prevaccin)
            prevaccin_data_json = json.loads(prevaccin_data)
            
            print(prevaccin_data_json["nom"])
            print(prevaccin_data_json["etat"])




            last_elevage = Elevage.objects.get(pk=prevaccin_data_json["elevage"])
            elevage_last = ElevageSerializer(last_elevage, many=False)
            last = elevage_last.data
            last_data = json.dumps(last)
            last_data_json = json.loads(last_data)
            print(last_data_json["type"])
            last_id = last_data_json["id"]


            class prevaccinKnowledge(KnowledgeEngine):
            
                @Rule(Fact(etat='Achevé'),Fact(nom='ANTI-STRESS'),Fact(type='Poule pondeuse'))
                def prevaccin2(self):
                    date = prevaccin_data_json["date_fin"]
                    date_init = datetime.datetime.strptime(date, "%Y-%m-%d")
                    date_days = date_init + timedelta(days=12)
                    date_days_deb_pre = date_init + timedelta(days=14)
                    date_days_fin_pre = date_init + timedelta(days=16)
                    date_prescrit = date_days.strftime("%Y-%m-%d")
                    date_deb_pre = date_days_deb_pre.strftime("%Y-%m-%d")
                    date_fin_pre = date_days_fin_pre.strftime("%Y-%m-%d")

                    prevaccin_data = {'elevage' : last_id , 'nom': 'ODIKANKANA 1', 'description': 'premier prise d''odikankana pendant 1 jours seulement','date_debut' : ''+date_prescrit+'' , 'date_fin': ''+date_prescrit+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    prevaccin_data1 = {'elevage' : last_id , 'nom': 'VITAMINE 2', 'description': 'Prise de vitamine sans medicaments Ex: VITAFLASH une(1) cuillere a soupe pour 5 litres d''eau ','date_debut' : ''+date_deb_pre+'' , 'date_fin': ''+date_fin_pre+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    
                    prevaccin_serializer = PrevaccinSerializer(data=prevaccin_data)
                    prevaccin_serializer1 = PrevaccinSerializer(data=prevaccin_data1)
                    if prevaccin_serializer.is_valid()&prevaccin_serializer1.is_valid():
                        prevaccin_serializer.save()
                        prevaccin_serializer1.save()
                        return JsonResponse(prevaccin_serializer.data, status=status.HTTP_201_CREATED)
                    return JsonResponse(prevaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
                @Rule(Fact(etat='Achevé'),Fact(nom='VITAMINE 2'),Fact(type='Poule pondeuse'))
                def prevaccin10(self):
                    date = prevaccin_data_json["date_debut"]
                    date_init = datetime.datetime.strptime(date, "%Y-%m-%d")
                    date_days = date_init + timedelta(days=5)
                    date_days_deb_pre = date_init + timedelta(days=4)
                    date_days_fin_pre = date_init + timedelta(days=6)
                    date_prescrit = date_days.strftime("%Y-%m-%d")
                    date_deb_pre = date_days_deb_pre.strftime("%Y-%m-%d")
                    date_fin_pre = date_days_fin_pre.strftime("%Y-%m-%d")

                    prevaccin_data1 = {'elevage' : last_id , 'nom': 'VACCIN Tad Pox ', 'description': 'Premier vaccin Tad Pox','date_debut' : ''+date_prescrit+'' , 'date_fin': ''+date_prescrit+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    prevaccin_data = {'elevage' : last_id , 'nom': 'VITAMINE 3', 'description': "Prise de vitamine avant , pendant et apres le vaccin Tad Pox Vitaflash ou Vitamax ou Antitox (15kg/L) ",'date_debut' : ''+date_deb_pre+'' , 'date_fin': ''+date_fin_pre+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    
                    prevaccin_serializer = PrevaccinSerializer(data=prevaccin_data)
                    prevaccin_serializer1 = PrevaccinSerializer(data=prevaccin_data1)
                    if prevaccin_serializer.is_valid()&prevaccin_serializer1.is_valid():
                        prevaccin_serializer1.save()
                        prevaccin_serializer.save()
                        return JsonResponse(prevaccin_serializer.data, status=status.HTTP_201_CREATED)
                    return JsonResponse(prevaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                @Rule(Fact(etat='Achevé'),Fact(nom='VITAMINE 3'),Fact(type='Poule pondeuse'))
                def prevaccin4(self):
                    date = prevaccin_data_json["date_debut"]
                    date_init = datetime.datetime.strptime(date, "%Y-%m-%d")
                    date_days = date_init + timedelta(days=8)
                    date_days_deb_pre = date_init + timedelta(days=7)
                    date_days_fin_pre = date_init + timedelta(days=9)
                    date_prescrit = date_days.strftime("%Y-%m-%d")
                    date_deb_pre = date_days_deb_pre.strftime("%Y-%m-%d")
                    date_fin_pre = date_days_fin_pre.strftime("%Y-%m-%d")

                    prevaccin_data1 = {'elevage' : last_id , 'nom': 'VACCIN La sota ', 'description': 'vaccin La sota , si y a pas beaucoup de poulet utiliser ITAnew','date_debut' : ''+date_prescrit+'' , 'date_fin': ''+date_prescrit+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    prevaccin_data = {'elevage' : last_id , 'nom': 'VITAMINE 4', 'description': "Prise de vitamine avant , pendant et apres le vaccin Tad Pox Vitaflash ou Vitamax ou Antitox (15kg/L) ",'date_debut' : ''+date_deb_pre+'' , 'date_fin': ''+date_fin_pre+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    
                    prevaccin_serializer = PrevaccinSerializer(data=prevaccin_data)
                    prevaccin_serializer1 = PrevaccinSerializer(data=prevaccin_data1)
                    if prevaccin_serializer.is_valid()&prevaccin_serializer1.is_valid():
                        prevaccin_serializer1.save()
                        prevaccin_serializer.save()
                        return JsonResponse(prevaccin_serializer.data, status=status.HTTP_201_CREATED)
                    return JsonResponse(prevaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                

                @Rule(Fact(etat='Achevé'),Fact(nom='VITAMINE 4'),Fact(type='Poule pondeuse'))
                def prevaccin3(self):
                    date = prevaccin_data_json["date_debut"]
                    date_init = datetime.datetime.strptime(date, "%Y-%m-%d")
                    date_days = date_init + timedelta(days=22 )
                    date_days_deb_pre = date_init + timedelta(days=24)
                    date_days_fin_pre = date_init + timedelta(days=26)
                    date_prescrit = date_days.strftime("%Y-%m-%d")
                    date_deb_pre = date_days_deb_pre.strftime("%Y-%m-%d")
                    date_fin_pre = date_days_fin_pre.strftime("%Y-%m-%d")

                    prevaccin_data1 = {'elevage' : last_id , 'nom': 'ODIKANKANA 2', 'description': 'Levasole 1 Sk/5 litres na Piperal 35k/5 litres ','date_debut' : ''+date_prescrit+'' , 'date_fin': ''+date_prescrit+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    prevaccin_data = {'elevage' : last_id , 'nom': 'VITAMINE 5', 'description': "Prise de vitamine avant , pendant et apres le vaccin Tad Pox Vitaflash ou Vitamax ou Antitox (15kg/L) ",'date_debut' : ''+date_deb_pre+'' , 'date_fin': ''+date_fin_pre+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    
                    prevaccin_serializer = PrevaccinSerializer(data=prevaccin_data)
                    prevaccin_serializer1 = PrevaccinSerializer(data=prevaccin_data1)
                    if prevaccin_serializer.is_valid()&prevaccin_serializer1.is_valid():
                        prevaccin_serializer1.save()
                        prevaccin_serializer.save()
                        return JsonResponse(prevaccin_serializer.data, status=status.HTTP_201_CREATED)
                    return JsonResponse(prevaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                @Rule(Fact(etat='Achevé'),Fact(nom='VITAMINE 5'),Fact(type='Poule pondeuse'))
                def prevaccin6(self):
                    date = prevaccin_data_json["date_debut"]
                    date_init = datetime.datetime.strptime(date, "%Y-%m-%d")
                    date_days = date_init + timedelta(days=5)
                    date_days_fin_pre = date_init + timedelta(days=9)
                    date_prescrit = date_days.strftime("%Y-%m-%d")
                    date_fin_pre = date_days_fin_pre.strftime("%Y-%m-%d")

                    prevaccin_data = {'elevage' : last_id , 'nom': 'AROATY', 'description': 'CARINTOL 1ml/Litre pendant 5 jours','date_debut' : ''+date_prescrit+'' , 'date_fin': ''+date_fin_pre+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    
                    prevaccin_serializer = PrevaccinSerializer(data=prevaccin_data)
                    if prevaccin_serializer.is_valid():
                        prevaccin_serializer.save()
                        return JsonResponse(prevaccin_serializer.data, status=status.HTTP_201_CREATED)
                    return JsonResponse(prevaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

                @Rule(Fact(etat='Achevé'),Fact(nom='AROATY'),Fact(type='Poule pondeuse'))
                def prevaccin8(self):
                    date = prevaccin_data_json["date_debut"]
                    date_init = datetime.datetime.strptime(date, "%Y-%m-%d")
                    date_days = date_init + timedelta(days=7)
                    date_days_deb_pre = date_init + timedelta(days=6)
                    date_days_fin_pre = date_init + timedelta(days=8)
                    date_prescrit = date_days.strftime("%Y-%m-%d")
                    date_deb_pre = date_days_deb_pre.strftime("%Y-%m-%d")
                    date_fin_pre = date_days_fin_pre.strftime("%Y-%m-%d")

                    prevaccin_data1 = {'elevage' : last_id , 'nom': 'VACCIN Itanew ou ND Bivalent', 'description': '','date_debut' : ''+date_prescrit+'' , 'date_fin': ''+date_prescrit+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    prevaccin_data = {'elevage' : last_id , 'nom': 'VITAMINE 7', 'description': "Prise de vitamine avant , pendant et apres le vaccin Tad Pox Vitaflash ou Vitamax ou Antitox (15kg/L) ",'date_debut' : ''+date_deb_pre+'' , 'date_fin': ''+date_fin_pre+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    
                    prevaccin_serializer = PrevaccinSerializer(data=prevaccin_data)
                    prevaccin_serializer1 = PrevaccinSerializer(data=prevaccin_data1)
                    if prevaccin_serializer.is_valid()&prevaccin_serializer1.is_valid():
                        prevaccin_serializer1.save()
                        prevaccin_serializer.save()
                        return JsonResponse(prevaccin_serializer.data, status=status.HTTP_201_CREATED)
                    return JsonResponse(prevaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

                @Rule(Fact(etat='Achevé'),Fact(nom='VITAMINE 7'),Fact(type='Poule pondeuse'))
                def prevaccin9(self):
                    date = prevaccin_data_json["date_debut"]
                    date_init = datetime.datetime.strptime(date, "%Y-%m-%d")
                    date_days = date_init + timedelta(days=79)
                    date_days_deb_pre = date_init + timedelta(days=71)
                    date_days_fin_pre = date_init + timedelta(days=73)
                    date_prescrit = date_days.strftime("%Y-%m-%d")
                    date_deb_pre = date_days_deb_pre.strftime("%Y-%m-%d")
                    date_fin_pre = date_days_fin_pre.strftime("%Y-%m-%d")

                    prevaccin_data = {'elevage' : last_id , 'nom': 'ANTICOCCIDIEN', 'description': " 1Sk pour 20 litres pendant trois (3) jours ",'date_debut' : ''+date_deb_pre+'' , 'date_fin': ''+date_fin_pre+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    prevaccin_data1 = {'elevage' : last_id , 'nom': 'VITAMINE 8', 'description': 'Vitaflash ou antitox ou diurimax 5j apres la fin de l"anticoccidien','date_debut' : ''+date_prescrit+'' , 'date_fin': ''+date_prescrit+'' , 'prix_unitaire': 0 , 'prix_total': 0 }

                    prevaccin_serializer = PrevaccinSerializer(data=prevaccin_data)
                    prevaccin_serializer1 = PrevaccinSerializer(data=prevaccin_data1)
                    if prevaccin_serializer.is_valid()&prevaccin_serializer1.is_valid():
                        prevaccin_serializer.save()
                        prevaccin_serializer1.save()
                        return JsonResponse(prevaccin_serializer.data, status=status.HTTP_201_CREATED)
                    return JsonResponse(prevaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


                @Rule(Fact(etat='Achevé'),Fact(nom='VITAMINE 8'),Fact(type='Poule pondeuse'))
                def prevaccin10(self):
                    date = prevaccin_data_json["date_debut"]
                    date_init = datetime.datetime.strptime(date, "%Y-%m-%d")
                    date_days = date_init + timedelta(days=13)
                    date_days_deb_pre = date_init + timedelta(days=12)
                    date_days_fin_pre = date_init + timedelta(days=14)
                    date_prescrit = date_days.strftime("%Y-%m-%d")
                    date_deb_pre = date_days_deb_pre.strftime("%Y-%m-%d")
                    date_fin_pre = date_days_fin_pre.strftime("%Y-%m-%d")

                    prevaccin_data1 = {'elevage' : last_id , 'nom': 'VACCIN La sota ', 'description': 'vaccin La sota , si y a pas beaucoup de poulet utiliser ITAnew','date_debut' : ''+date_prescrit+'' , 'date_fin': ''+date_prescrit+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    prevaccin_data = {'elevage' : last_id , 'nom': 'VITAMINE 9', 'description': "Prise de vitamine avant , pendant et apres le vaccin Tad Pox Vitaflash ou Vitamax ou Antitox (15kg/L) ",'date_debut' : ''+date_deb_pre+'' , 'date_fin': ''+date_fin_pre+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    
                    prevaccin_serializer = PrevaccinSerializer(data=prevaccin_data)
                    prevaccin_serializer1 = PrevaccinSerializer(data=prevaccin_data1)
                    if prevaccin_serializer.is_valid()&prevaccin_serializer1.is_valid():
                        prevaccin_serializer1.save()
                        prevaccin_serializer.save()
                        return JsonResponse(prevaccin_serializer.data, status=status.HTTP_201_CREATED)
                    return JsonResponse(prevaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                @Rule(Fact(etat='Achevé'),Fact(nom='VITAMINE 9'),Fact(type='Poule pondeuse'))
                def prevaccin10(self):
                    date = prevaccin_data_json["date_debut"]
                    date_init = datetime.datetime.strptime(date, "%Y-%m-%d")
                    date_days = date_init + timedelta(days=85)
                    date_days_deb_pre = date_init + timedelta(days=84)
                    date_days_fin_pre = date_init + timedelta(days=86)
                    date_prescrit = date_days.strftime("%Y-%m-%d")
                    date_deb_pre = date_days_deb_pre.strftime("%Y-%m-%d")
                    date_fin_pre = date_days_fin_pre.strftime("%Y-%m-%d")

                    prevaccin_data1 = {'elevage' : last_id , 'nom': 'VACCIN La sota ', 'description': 'vaccin La sota , si y a pas beaucoup de poulet utiliser ITAnew (repetition toutes les 12 semaines)','date_debut' : ''+date_prescrit+'' , 'date_fin': ''+date_prescrit+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    prevaccin_data = {'elevage' : last_id , 'nom': 'VITAMINE 9', 'description': "Prise de vitamine avant , pendant et apres le vaccin Tad Pox Vitaflash ou Vitamax ou Antitox (15kg/L) ",'date_debut' : ''+date_deb_pre+'' , 'date_fin': ''+date_fin_pre+'' , 'prix_unitaire': 0 , 'prix_total': 0 }
                    
                    prevaccin_serializer = PrevaccinSerializer(data=prevaccin_data)
                    prevaccin_serializer1 = PrevaccinSerializer(data=prevaccin_data1)
                    if prevaccin_serializer.is_valid()&prevaccin_serializer1.is_valid():
                        prevaccin_serializer1.save()
                        prevaccin_serializer.save()
                        return JsonResponse(prevaccin_serializer.data, status=status.HTTP_201_CREATED)
                    return JsonResponse(prevaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            engine = prevaccinKnowledge()
            engine.reset()
            engine.declare(Fact(etat = prevaccin_data_json["etat"]),Fact(nom=prevaccin_data_json["nom"]),Fact(type=last_data_json["type"]))
            engine.run()
            return JsonResponse(prevaccin_serializer.data)
        return JsonResponse(prevaccin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

######################################################################################
#Eau

@api_view(['GET', 'POST', 'DELETE'])
def eau_list(request):
   if request.method == 'GET':

        nourriture = Eau.objects.all()

        eau_serializer = EauSerializer(eau, many=True)
        return JsonResponse(eau_serializer.data, safe=False)

   elif request.method == 'POST':
        eau_data = JSONParser().parse(request)
        eau_serializer = EauSerializer(data=eau_data)
        if eau_serializer.is_valid():
            eau_serializer.save()
            return JsonResponse(eau_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(eau_serializer.errors, status=status.HTTP_400_BAD_REQUEST)