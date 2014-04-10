import calendar
import datetime
from django.shortcuts import render
from django.views.generic import View
from .models import Team

# Create your views here.

class Home(View):
    def get(self, request):
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
