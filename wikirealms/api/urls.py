from django.urls import path
from .views import *

urlpatterns = [
     # api url for a list of all the realms (at all!!)
     path('realms/', Realms.as_view(), name='realms'),
     # api url for a single realm!
     path('realms/<int:id>/', RealmDetail.as_view(), name='realm_detail'),
     # api url for all the realm pages (at all!)
     path('realm_pages/', RealmPages.as_view(), name='realm_pages'),
     # api url for all the characters (at all!)
     path('characters/', Characters.as_view(), name='characters'),
     # api url for all the settings (at all!)
     path('settings/', Settings.as_view(), name='settings'),

]

