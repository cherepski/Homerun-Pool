from django.core.management.base import BaseCommand
from homerun.homerun_app.models import Team, Player
import csv

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		with open('sample_team_load.csv', 'rb') as f:
			reader = csv.reader(f)
			counter = 0
			Team.objects.all().delete()
			Player.objects.all().delete()
			team_list = []
			for row in reader:
				if counter == 0 or counter % 8 == 0:
					del team_list[:]
					for team in row:
						team_obj = Team()
						team_obj.name = team
						team_obj.save()
						team_list.append(team_obj)
				else:
					player_counter = 0
					for player in row:
						if not Player.objects.filter(name=player):
							player_obj = Player()
							player_obj.name = player
							player_obj.save()
							team_obj = team_list[player_counter]
							team_obj.player.add(player_obj)
						else:
							player_obj = Player.objects.get(name=player)
							team_obj = team_list[player_counter]
							team_obj.player.add(player_obj)
						player_counter = player_counter + 1
				counter = counter + 1
