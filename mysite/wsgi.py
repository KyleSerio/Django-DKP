"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import os
import sys
#
## assuming your django settings file is at '/home/KSerio/mysite/mysite/settings.py'
## and your manage.py is is at '/home/KSerio/mysite/manage.py'
path = '/home/KSerio/Django-DKP'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)
#
#
## then:

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
