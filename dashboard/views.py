from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def Index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def TimelineView(request):
    return render(request, 'timeline.html')


@login_required(login_url='login')
def CalendarView(request):
    return render(request, 'calendar.html')


@login_required(login_url='login')
def CalculateView(request):
    return render(request, 'chart-morris.html')


@login_required(login_url='login')
def ReportView(request):
    return render(request, 'export-table.html')


@login_required(login_url='login')
def WeatherView(request):
    return render(request, 'weather.html')


@login_required(login_url='login')
def GeoMapsView(request):
    return render(request, 'gmaps-geolocation.html')


@login_required(login_url='login')
def ProfileView(request):
    return render(request, 'profile.html')