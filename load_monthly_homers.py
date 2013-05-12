import sys
import csv
from homerun.homerun_app.models import Team, Team_Month

month = sys.argv[1]
input_file = sys.argv[2]

with open(input_file, 'r') as file:
	rowreader = csv.reader(file)
	for row in rowreader:
		team_month = Team_Month(team=Team.objects.get(name__iexact=row[1]), key=month, value=row[2])
		team_month.save()
