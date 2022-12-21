from django.shortcuts import render


# Create your views here.

def  creatorDashboardPageView(request) :
   return render(request, 'worldbuilding/worldbuilding.html')



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    VIEWS RELATED TO WORLDS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

def createWorldPageView(request) :
   return render(request, 'worldbuilding/create_world.html')

def worldPageView(request) :
   return render(request, 'worldbuilding/world.html')

def editWorldPageView(request) :
   return render(request, 'worldbuilding/edit_world.html')




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    VIEWS RELATED TO CHARACTERS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

def characterPageView(request) :
   return render(request, 'worldbuilding/character.html')

def editCharacterPageView(request) :
   return render(request, 'worldbuilding/edit_character.html')





# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    VIEWS RELATED TO PLOTS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def plotArcPageView(request) :
   return render(request, 'worldbuilding/plot_arc.html')

def editPlotArcPageView(request) :
   return render(request, 'worldbuilding/edit_plot_arc.html')
