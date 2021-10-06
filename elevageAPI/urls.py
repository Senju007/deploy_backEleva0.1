from django.conf.urls import url
from elevageAPI import views

from rest_framework import routers
from elevageAPI.views import ElevageViewSet

router = routers.DefaultRouter()
router.register('elevage2',ElevageViewSet)

urlpatterns = [
         url(r'^elevageAPI/elevage$', views.elevage_list),
         url(r'^elevageAPI/vaccin$', views.vaccin_list),
         url(r'^elevageAPI/stock$', views.stock),
         url(r'^elevageAPI/prevaccin$', views.prevaccin),
         url(r'^elevageAPI/poulette$', views.poulette),
         url(r'^elevageAPI/pondeuseI$', views.pondeuseI),
         url(r'^elevageAPI/pondeuseII$', views.pondeuseII),
         url(r'^elevageAPI/pondeuseIII$', views.pondeuseIII),
         url(r'^elevageAPI/user$', views.user),
         url(r'^elevageAPI/nourriture$', views.nourriture_list),
         url(r'^elevageAPI/elevage/nombre', views.elevage_nombre),
         url(r'^elevageAPI/elevage/totalN/(?P<pk>[0-9]+)$', views.elevage_nourriture_total),
         url(r'^elevageAPI/elevage/last', views.elevage_last),
         url(r'^elevageAPI/vaccin/(?P<pk>[0-9]+)$', views.vaccin_detail),
         url(r'^elevageAPI/elevage/(?P<pk>[0-9]+)$', views.elevage_detail),
         url(r'^elevageAPI/nourriture/(?P<pk>[0-9]+)$', views.nourriture_detail),
         url(r'^elevageAPI/prevaccin/(?P<pk>[0-9]+)$', views.prevaccin_detail),
         url(r'^elevageAPI/elevage/nourriture/(?P<pk>[0-9]+)$', views.elevage_nourriture),
         url(r'^elevageAPI/nourriture/fin2j', views.notification_nourriture),
         url(r'^elevageAPI/prevaccin/deb2j', views.notification_soins),
]