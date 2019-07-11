from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  index_dict = {'indexContext':'Index of Page'}
  return render(request,'cv/index.html',context=index_dict)


def help(request):
  help_dict = {'helpContext':'This is Help Page'}
  return render(request,'cv/help.html',context=help_dict)