from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

# @api_view(['GET'])
# def realm_list(request):
#    realms = Realm.objects.all()
#    data = {'realms': list(realms.values())}
#    return JsonResponse(data)
#



def  creatorDashboardPageView(request) :
   return render(request, 'worldbuilding/worldbuilding.html')



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    REALM PAGE VIEWS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

def createRealmPageView(request) :
   return render(request, 'worldbuilding/create_realm.html')

def viewRealmPageView(request) :
   return render(request, 'worldbuilding/realm.html')

def editRealmPageView(request) :
   return render(request, 'worldbuilding/edit_realm.html')




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    CHARACTERS VIEWS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

def characterPageView(request) :
   return render(request, 'worldbuilding/character.html')

def editCharacterPageView(request) :
   return render(request, 'worldbuilding/edit_character.html')





# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    PLOTS VIEWS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def viewPlotArcPageView(request) :
   return render(request, 'worldbuilding/plot_arc.html')

def editPlotArcPageView(request) :
   return render(request, 'worldbuilding/edit_plot_arc.html')



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    OTHER PAGE VIEWS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def viewOtherPageView(request) :
   return render(request, 'worldbuilding/other.html')

def editOtherPageView(request) :
   return render(request, 'worldbuilding/edit_other.html')


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    CONTENT BLOCK VIEWS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def addContentBlockView(request) :
   return render(request, 'worldbuilding/add_content_block.html')

def editContentBlockView(request) :
   return render(request, 'worldbuilding/edit_content_block.html')
