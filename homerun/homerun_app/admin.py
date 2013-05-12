from django.contrib import admin
from homerun.homerun_app.models import Player, Team, Team_Month

class PlayerAdmin(admin.ModelAdmin):
	pass

class TeamAdmin(admin.ModelAdmin):
	pass

class TeamMonthAdmin(admin.ModelAdmin):
	pass

admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Team_Month, TeamMonthAdmin)
