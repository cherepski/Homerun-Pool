#!/bin/bash
cd /srv/www/Homerun-Pool
source virtpy/bin/activate
cd homerun_pool
python manage.py pull_homers
