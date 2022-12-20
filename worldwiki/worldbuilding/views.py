from django.shortcuts import render


# Create your views here.

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    VIEWS RELATED TO WORLDS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def worldPageView(request) :
   return render(request, 'wiki/world.html')

def editWorldPageView(request) :
   return render(request, 'wiki/edit_world.html')




# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    VIEWS RELATED TO CHARACTERS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

def characterPageView(request) :
   return render(request, 'wiki/character.html')

def editCharacterPageView(request) :
   return render(request, 'wiki/edit_character.html')





# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    VIEWS RELATED TO PLOTS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def plotArcPageView(request) :
   return render(request, 'wiki/plot_arc.html')

def editPlotArcPageView(request) :
   return render(request, 'wiki/edit_plot_arc.html')
