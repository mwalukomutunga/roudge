from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Create your views here.
from .models import Events


def index(request):
    Lastest_events = Events.objects.all()[:10]
    return render(request, 'events/index.html', {
        'events': Lastest_events
    })


def blog(request):
    return render(request, 'events/blog.html')
