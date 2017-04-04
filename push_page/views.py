from django.shortcuts import render
from .models import *

# Create your views here.

def push_page(request,quick_page):
    archives = PushPage.objects.all()
    page = PushPage.objects.get(id=quick_page)
    context = {'page':page,'archives':archives}
    return render(request,'push_page/Push_Page.html',context)
