from django.urls import path
from .views import *

urlpatterns = [
    # wiki pages urls
    path('view_wiki/', viewWikiPagePageView, name='viewWikiPage'),
    path('edit_wiki/', editWikiPagePageView, name='editWikiPage'),   
]