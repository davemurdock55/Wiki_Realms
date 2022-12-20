from django.shortcuts import render


# Create your views here.

# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    VIEWS RELATED TO GENERIC WIKI PAGES    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

def viewWikiPagePageView(request) :
   return render(request, 'wiki/wiki_page.html')   
 
def editWikiPagePageView(request) :
   return render(request, 'wiki/edit_wiki_page.html')     