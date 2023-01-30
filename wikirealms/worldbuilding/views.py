from django.shortcuts import render


# Create your views here.

def  creatorDashboardPageView(request) :
   return render(request, 'worldbuilding/worldbuilding.html')



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    REALM PAGE VIEWS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

def createWorldPageView(request) :
   return render(request, 'worldbuilding/create_world.html')

def viewWorldPageView(request) :
   return render(request, 'worldbuilding/world.html')

def editWorldPageView(request) :
   return render(request, 'worldbuilding/edit_world.html')




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
