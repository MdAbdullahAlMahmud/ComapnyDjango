from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact

def contact(request):

    if request.method=='POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        subject= request.POST.get('subject')
        message= request.POST.get('message')

        contact = Contact()
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message

        contact.save()
        
    return render(request,'contact.html')

  