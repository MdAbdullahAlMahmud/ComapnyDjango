from django.http import HttpResponse
from django.shortcuts import render
from .models import about
from .models import slider


def home(request):
    data= about.objects.all()
    slide = slider.objects.all() 
    context = {
       'about':data,
       'slide':slide
    }
    print(data)
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'about.html')

# def contactus(request):
#     return render(request,'contact.html')   
   
