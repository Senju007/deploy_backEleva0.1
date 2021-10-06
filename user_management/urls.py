from rest_framework import routers
from user_management.views import MeViewSet  , GetCSRFToken
from django.urls import path

router = routers.DefaultRouter()

router.register('me' , MeViewSet , basename = 'me')
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('csrf_cookie/', csrf_exempt(GetCSRFToken.as_view()))
]