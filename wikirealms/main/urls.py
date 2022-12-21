from django.urls import path
from .views import *

urlpatterns = [
    path('login/', loginPageView, name='login'),
    path('signup/', signupPageView, name='signup'),
    path('', indexPageView, name='home'),
]
