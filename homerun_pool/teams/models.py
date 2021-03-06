import datetime
from django.db import models
from django.db.models import Sum

# Create your models here.

MONTH_CHOICES=(('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'))

class Player(models.Model):
	name = models.CharField(max_length=255, unique=True)
	mlb_id = models.IntegerField(null=True)
	homerun = models.IntegerField(default=0)
	hot = models.IntegerField(default=0)
	def __unicode__(self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=255)
	player = models.ManyToManyField(Player)
	earnings = models.IntegerField(default=0)
	def __unicode__(self):
		return self.name

	@property
	def homerun_total(self):
		return self.player.aggregate(Sum('homerun'))['homerun__sum']

	@property
	def hot_total(self):
		return self.player.aggregate(Sum('hot'))['hot__sum']

	@property
	def month_total(self):
                if datetime.datetime.now().month == 10:
			return self.homerun_total - TeamMonth.objects.filter(team=self).exclude(key__iexact="September").aggregate(Sum('value'))['value__sum']
		try:
			return self.homerun_total - TeamMonth.objects.filter(team=self).aggregate(Sum('value'))['value__sum']
		except TypeError, e:
			return self.homerun_total

class TeamMonth(models.Model):
	team = models.ForeignKey(Team)
	key = models.CharField(max_length=255, choices=MONTH_CHOICES)
	value = models.IntegerField(default=0)

	class Meta:
		unique_together = ('team', 'key')
	def __unicode__(self):
		return "%s %s %s" % (str(self.team), self.key, str(self.value))
