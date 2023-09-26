from django.shortcuts import render 
from . models import Shops
from django.contrib.auth.models import User
import requests
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    item=Shops.objects.all()
    return render(request,"index.html",{"item":item})

def detial(request,id):
    detial=Shops.objects.get(id=id)
    return render(request,"detial.html",{'detial':detial})
                               

