from django.core.management.base import BaseCommand
from teams.models import Team, Player, TeamMonth
import csv

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		with open('teams/management/commands/team_load.csv', 'rb') as f:
			reader = csv.reader(f)
			Team.objects.all().delete()
			Player.objects.all().delete()
                        TeamMonth.objects.all().delete()
			team_list = []
			for index, row in enumerate(reader):
				if index == 0 or index % 8 == 0:
					team_list[:] = []
					for name in row:
						team_obj = Team()
						team_obj.name = name
						team_obj.save()
						team_list.append(team_obj)
				else:
					for index, name in enumerate(row):
						player, created = Player.objects.get_or_create(name=name)
						team_list[index].player.add(player)
