import os, sys
from django.core.handlers.wsgi import WSGIHandler

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)))

os.environ["DJANGO_SETTINGS_MODULE"] = "djProject.settings"
application = WSGIHandler()

