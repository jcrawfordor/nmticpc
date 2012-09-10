import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nmticpc.settings")

sys.path.append("/var/www-icpc/")
sys.path.append("/var/www-icpc/nmticpc")

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
