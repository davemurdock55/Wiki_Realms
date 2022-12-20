from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from hashlib import sha256
from datetime import date
from datetime import datetime
import re

# For password hashing (salting)
salt = '2%5!#b2wr3SIs601c616f509c7b2374ffa12ef51d3d0bcfa511c2e7e8d4e4a5cbd678b7cf5e!#$12ef51d3d0bcfa511c$@1saTeRwq093&2jsfld'


# loggedIn Function
# This function checks if the user is logged in and returns a True value to logged_in if the user IS logged in
def loggedIn(request) :
    # Setting the logged_in variable to False
    logged_in = False

    # if the user's userid is found in the session storage
    if 'userid' in request.session :
        # if the user's userid is not None
        if not request.session['userid'] == None :
            # get the user's information from the database
            user = Person.objects.get(id=request.session['userid'])
            # set the logged_in variable to True
            logged_in = True
        # else (if the user's userid is None)
        else :
            # set the user variable to None
            user = None
    # else (if the user's userid is not found in the session storage)
    else :
        # set the user variable to None
        user = None

    # return the logged_in variable and the user variable
    return logged_in, user



# Create your views here.

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    VIEWS RELATED TO USER ACCOUNT    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

def loginPageView(request) :
    error = False
    logged_in, user = loggedIn(request)

    print('login view ' + request.method)

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        usernames = Person.objects.values_list('username')

        for name in usernames :
            print(name[0])
            
        if len(usernames) > 0 :
            for name in usernames :
                if username == name[0] :
                    user = Person.objects.get(username=username)
                    hash_password = sha256((password + salt[0:(len(password) + len(username))]).encode('utf-8')).hexdigest()

                    if hash_password == user.password :
                        request.session['userid'] = user.id
                        return redirect(indexPageView)

                    else :
                        error = True
                else :
                    error = True
        else :
            error = True

    context = {
        'error': error,
        'logged_in' : logged_in,
        'user' : user,
        'title' : 'Log in'
    }

    return render(request, 'main/login.html')


def signupPageView(request) :
   return render(request, 'main/signup.html')



# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    VIEWS RELATED TO THE MAIN/HOME PAGES    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

def indexPageView(request) :
    logged_in, user = loggedIn(request)
    
    context = {
        'logged_in' : logged_in,
        'user' : user,
    }

    return render(request, 'main/index.html', context)


