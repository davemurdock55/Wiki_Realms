from django.urls import path
from .views import *

urlpatterns = [
    # root urls
    path('creator_dashboard/', creatorDashboardPageView, name='creator_dashboard'),
    
    # world urls
    path('create_realm/', createRealmPageView, name='create_realm'),
    path('view_realm/', viewRealmPageView, name='view_realm'),
    path('edit_realm/', editRealmPageView, name='edit_realm'),
    # character urls
    path('view_character/', characterPageView, name='view_character'),
    path('edit_character/', editCharacterPageView, name='edit_character'),
    # plot arc urls
    path('view_plot_arc/', viewPlotArcPageView, name='view_plot_arc'),
    path('edit_plot_arc/', editPlotArcPageView, name='edit_plot_arc'),
    # other page urls
    path('view_other_page/', viewOtherPageView, name='view_other_page'),
    path('edit_other_page/', editOtherPageView, name='edit_other_page'),
]

