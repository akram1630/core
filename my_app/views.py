from django.shortcuts import render

# Create your views here.
#bismillah :

from django.http import HttpResponse


#function to response the user :
# request of user
def index(request):
  return HttpResponse('Hello Mohammed Akram')
  #it prints in screen
