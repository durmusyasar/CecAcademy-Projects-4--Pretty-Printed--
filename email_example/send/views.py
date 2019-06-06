from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    send_mail(
        'Helloooo',
        'Hiiii',
        'durmusyasar13@gmail.com',
        ['gagusexi@safe-planet.com'],
        fail_silently=False
    )
    return(request, 'send/index.html')