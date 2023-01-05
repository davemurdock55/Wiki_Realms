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
    # Setting the error variable to False
    error = False
    # Getting the logged_in and user variables from the loggedIn function (using the request)
    logged_in, user = loggedIn(request)

    # print "login view" along with the request's method to the console
    print('login view ' + request.method)

    # if the request's method is POST
    if request.method == 'POST' :
        # get the username from the request
        username = request.POST['username']
        # get the password from the request
        password = request.POST['password']
        # get all the usernames from the database that match the username from the request
        usernames = Person.objects.values_list('username')

        # print all the usernames to the console (was this for bugfixing or something?)
        # for each username among all the usernames in the database
        for name in usernames :
            # print that username to the console
            print(name[0])
        
        # if there are more than one username that match
        if len(usernames) > 0 :
            # for each username among all the usernames in the database that match the username from the request
            for name in usernames :
                # if the "name" username matches the username from the request
                if username == name[0] :
                    # get the user's information from the database
                    user = Person.objects.get(username=username)
                    # hash the password using the salt
                    hash_password = sha256((password + salt[0:(len(password) + len(username))]).encode('utf-8')).hexdigest()

                    # if the hashed password is the same as the user's password
                    if hash_password == user.password :
                        # set the user's id to the session storage
                        request.session['userid'] = user.id
                        # then redirect to the indexPageView function
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

    return render(request, 'main/login.html', context)


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


