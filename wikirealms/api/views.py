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
     


# 
# @api_view(['GET'])
# def realm_list(request): 
#      
#      email = request.session['email']
#      user = User.objects.get(email=email)  
# 
#      # getting all the entries in the Realms table
#      realms = Realm.objects.all()
#      # getting the data from the table and putting it into a dictionary
#      data = {'realms': list(realms.values())}
#      return JsonResponse(data)
# 
# @api_view(['GET'])
# def realm_pages(request):
#      # get all the pages in the realm
#      pages = Page.objects.all()
#      return(Response({'pages': list(pages.values())}))
# 
# 
# @api_view(['GET'])
# def HelloWorldView(request):
#      # print("Hello, world! ! ! ! ! ! ! ! ! ! \n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!\n!")
#      return Response({'message': 'Hello, world!'})
