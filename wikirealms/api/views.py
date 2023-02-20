from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from worldbuilding.models import *


# Create your views here.

app_name = 'api'

class HelloWorldView(APIView):
     def get(self, request):
          return Response({'message': 'Hello, world!'})


class Realms(APIView):
     def get(self, request):
          realms = Realm.objects.all()
          data = {'realms': list(realms.values())}
          return Response(data)


class RealmPages(APIView):
     def get(self, request):
          realm_pages = Page.objects.all()
          data = {'pages': list(realm_pages.values())}
          return Response(data)
     

class Characters(APIView):
     def get(self, request):
          characters = Character.objects.all()
          data = {'pages': list(characters.values())}
          return Response(data)
     
class Settings(APIView):
     def get(self, request):
          settings = Setting.objects.all()
          data = {'pages': list(settings.values())}
          return Response(data)
