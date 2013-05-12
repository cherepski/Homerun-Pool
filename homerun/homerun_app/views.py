# Create your views here.
from django.shortcuts import render
from homerun.homerun_app.models import Team, Player, Team_Month
import calendar
import datetime

def home(request):
	teams = sorted(Team.objects.all(), key=lambda a: a.homerun_total, reverse=True)
	month_teams = sorted(Team.objects.all(), key=lambda a: a.month_total, reverse=True)
	hot_teams = sorted(Team.objects.all(), key=lambda a: a.hot_total, reverse=True)[0:3]
	for team in teams:
		if team in hot_teams:
			team.hot = True
	return render(request, 'index.html', {
		'teams': teams,
		'month_teams': month_teams,
		'current_month': calendar.month_name[datetime.datetime.today().month]
	})
