from django.core.management.base import BaseCommand
from django.db.models import Sum
from homerun.homerun_app.models import Team, Player, Team_Month
import calendar
import urllib2
import json
import datetime

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		for player in Player.objects.all():
			raw_result = urllib2.urlopen("http://mlb.mlb.com/lookup/json/named.mlb_bio_hitting_last_10.bam?results=200&game_type='R'&season=2013&player_id={}&mlb_individual_hitting_last_x_total.col_in=game_date&mlb_individual_hitting_last_x_total.col_in=opp&mlb_individual_hitting_last_x_total.col_in=ab&mlb_individual_hitting_last_x_total.col_in=r&mlb_individual_hitting_last_x_total.col_in=h&mlb_individual_hitting_last_x_total.col_in=hr&mlb_individual_hitting_last_x_total.col_in=rbi&mlb_individual_hitting_last_x_total.col_in=bb&mlb_individual_hitting_last_x_total.col_in=so&mlb_individual_hitting_last_x_total.col_in=sb&mlb_individual_hitting_last_x_total.col_in=avg&mlb_individual_hitting_last_x_total.col_in=home_away&mlb_individual_hitting_last_x_total.col_in=game_id&mlb_individual_hitting_last_x_total.col_in=game_type".format(player.mlb_id))
			json_parse = json.load(raw_result)
			try:
				player.homerun = json_parse['mlb_bio_hitting_last_10']['mlb_individual_hitting_last_x_total']['queryResults']['row']['hr']
			except KeyError:
				player.homerun = 0

			raw_result = urllib2.urlopen("http://mlb.mlb.com/lookup/json/named.mlb_bio_hitting_last_10.bam?results=3&game_type='R'&season=2013&player_id={}&mlb_individual_hitting_last_x_total.col_in=game_date&mlb_individual_hitting_last_x_total.col_in=opp&mlb_individual_hitting_last_x_total.col_in=ab&mlb_individual_hitting_last_x_total.col_in=r&mlb_individual_hitting_last_x_total.col_in=h&mlb_individual_hitting_last_x_total.col_in=hr&mlb_individual_hitting_last_x_total.col_in=rbi&mlb_individual_hitting_last_x_total.col_in=bb&mlb_individual_hitting_last_x_total.col_in=so&mlb_individual_hitting_last_x_total.col_in=sb&mlb_individual_hitting_last_x_total.col_in=avg&mlb_individual_hitting_last_x_total.col_in=home_away&mlb_individual_hitting_last_x_total.col_in=game_id&mlb_individual_hitting_last_x_total.col_in=game_type".format(player.mlb_id))
                        json_parse = json.load(raw_result)
                        try:
                                player.hot = json_parse['mlb_bio_hitting_last_10']['mlb_individual_hitting_last_x_total']['queryResults']['row']['hr']
                        except KeyError:
                                player.hot = 0

			player.save()
		if datetime.date.today().day == 1:
			for team in Team.objects.all():
				team_month = Team_Month()
				team_month.team = team
				team_month.key = calendar.month_name[datetime.date.today().month - 1]
				if Team_Month.objects.filter(team=team).aggregate(Sum('value'))['value__sum']:
					team_month.value = team.player.aggregate(Sum('homerun'))['homerun__sum'] - Team_Month.objects.filter(team=team).aggregate(Sum('value'))['value__sum']
				else:
					team_month.value = team.player.aggregate(Sum('homerun'))['homerun__sum']
				team_month.save()
