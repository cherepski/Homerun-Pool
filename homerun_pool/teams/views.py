import calendar
import datetime
from django.shortcuts import render
from django.views.generic import View
from .models import Team, TeamMonth

# Create your views here.

class Home(View):
    def get(self, request):
	month_teams = sorted(Team.objects.prefetch_related('player').all(), key=lambda a: a.month_total, reverse=True)
	return render(request, 'index.html', {
		'month_teams': month_teams,
		'current_month': calendar.month_name[datetime.datetime.today().month]
	})

class Season(View):
    def get(self, request):
        teams = sorted(Team.objects.prefetch_related('player').all(), key=lambda a: a.homerun_total, reverse=True)
	return render(request, 'season.html', {'teams': teams, 'active': 'season'})

class Money(View):
    def get(self, request):
        teams = Team.objects.all().order_by('-earnings')
	return render(request, 'money.html', {'teams': teams, 'active': 'money'})

class Month(View):
    def get(self, request, month):
    	if month == calendar.month_name[datetime.datetime.today().month]:
	    return Home.as_view()(self.request)

        teams = TeamMonth.objects.filter(key=month).order_by('-value')
	return render(request, 'month.html', {'teams': teams, 'month': month})
