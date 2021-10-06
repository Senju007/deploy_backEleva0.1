from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user_management.serializers import UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework import permissions

# Create your views here.
class MeViewSet(viewsets.ViewSet):
    def list(self , request):
        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return Response(user_data)

@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFToken(APIView):
    permission_classes = (permissions.AllowAny, ) 

    def get(self, request, format=None):
        return Response({ 'success': '+CSRF cookie set+',  } )