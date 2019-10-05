from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Videos


def index(request):
    return render(request, 'home/index.html')


def services(request):
    return render(request, 'home/services.html')


def contacts(request):
    return render(request, 'home/contact.html')


def video(request):
    vedios_list = Videos.objects.all()[:10]
    return render(request, 'home/videos.html', {
        'Videos_list': vedios_list
    })


def gallery(request):
    return render(request, 'home/gallery.html')
