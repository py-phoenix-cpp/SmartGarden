from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('', Index, name='index'),
    path('timeline/', TimelineView, name='timeline'),
    path('calendar/', CalendarView, name='calendar'),
    path('calculate/', CalculateView, name='calculate'),
    path('report/', ReportView, name='report'),
    path('weather/', WeatherView, name='weather'),
    path('geo-maps/', GeoMapsView, name='geo-maps'),
    path('profile/', ProfileView, name='profile'),
]
