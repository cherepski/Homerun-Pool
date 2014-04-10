import os, sys, site

workspace = os.path.abspath('%s/../../..' % os.path.dirname(__file__))

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('%s/.env/lib/python2.6/site-packages' % workspace)

# Add the app's directory to the PYTHONPATH
sys.path.append('%s/homerun-pool/homerun_pool' % workspace)

# Activate your virtual env
activate_env=os.path.expanduser("%s/.env/bin/activate_this.py" % workspace)
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'homerun_pool.settings'

    return _application(environ, start_response)
