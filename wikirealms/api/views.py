from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from worldbuilding.models import *


# Create your views here.

app_name = 'api'


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

class RealmDetail(APIView):
     def get(self, request, id):
          realm = Realm.objects.filter(id=id).first()
          if not realm:
               return Response({'message': 'Realm not found'}, status=404)

          pages = Page.objects.filter(realm_id=id)
          characters = Character.objects.filter(pages__in=pages).distinct()
          settings = Setting.objects.filter(pages__in=pages).distinct()

          data = {
               'id': realm.id,
               'title': realm.name,
               'description': realm.description,
               'image': request.build_absolute_uri(realm.image.url) if realm.image else None,
               'pages': list(pages.values()),
               'characters': list(characters.values()),
               'settings': list(settings.values())
          }


          return Response(data)
