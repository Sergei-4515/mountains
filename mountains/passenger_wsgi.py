# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/r/ru4515kq/ru4515kq.beget.tech/mountains')
sys.path.insert(1, '/home/r/ru4515kq/ru4515kq.beget.tech/venv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mountains.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()