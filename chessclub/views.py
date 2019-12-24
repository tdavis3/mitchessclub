from django.shortcuts import render
import datetime

now = datetime.datetime.now()


# Create your views here.

def index(request):
    return render(request, 'chessclub/index.html', {'nav_item': 1, 'year': now.year})

def events(request):
    return render(request, 'chessclub/events.html', {'nav_item': 2, 'year': now.year})

def team(request):
    return render(request, 'chessclub/team.html', {'nav_item': 3, 'year': now.year})

def sponsors(request):
    return render(request, 'chessclub/sponsors.html', {'nav_item': 4, 'year': now.year})

def contact(request):
    return render(request, 'chessclub/contact.html', {'nav_item': 5, 'year': now.year})

def upcoming_event(request):
    return render(request, 'chessclub/upcoming_event.html', {'year': now.year})
