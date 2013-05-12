Homerun-Pool
============

Web app which allows for the creation of a homerun type office pool thingy

Installation:
This is a Django app so please install as such.  Should be relatively straight forward if you know Django.  I've removed the settings.py file so you will have to add your own.

Overview:
Django app to run a homerun pool for your office or your firends or whoever.  Each team will be given a Team model.  Each Team is allowed to choose X number of players in the MLB and after each month, the team with the most homeruns hits total wins that month and also the team with the most homerun at the end of the season wins the complete season.

Management Commands:
There are two management commands in there that pull homeruns for each player in the leagues and also a command to load teams for a csv file.  See the samples.
