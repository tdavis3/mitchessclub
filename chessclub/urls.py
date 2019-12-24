from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('team/', views.team, name='team'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('contact/', views.contact, name='contact'),
    path('upcoming_event/', views.upcoming_event, name='upcoming_event'),
]
