# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings

from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm

def index(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'GET':
        form =  ContactForm()

    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, from_email, ['pedro.social.isw@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact')
    return render(request, 'contact.html', context={'form':form})

def about(request):
    return render(request, 'about-me.html')