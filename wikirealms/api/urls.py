from django.urls import path
from .views import *

urlpatterns = [
     path('hello/', HelloWorldView.as_view(), name='hello_world'),
     # api url for a realms list
     path('realms/', Realms.as_view(), name='realms'),
     # api url for a realm pages
     path('realm_pages/', RealmPages.as_view(), name='realm_pages'),
     # api url for hello world (test)
     
]

