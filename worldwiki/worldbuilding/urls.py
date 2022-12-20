from django.urls import path
from .views import *

urlpatterns = [
    # world urls
    path('view_world/', worldPageView, name='viewWorld'),
    path('edit_world/', editWorldPageView, name='editWorld'),
    # character urls
    path('view_character/', characterPageView, name='viewCharacter'),
    path('edit_character/', editCharacterPageView, name='editCharacter'),
    # plot arc urls
    path('view_plot_arc/', plotArcPageView, name='viewPlotArc'),
    path('edit_plot_arc/', editPlotArcPageView, name='editPlotArc'),
]