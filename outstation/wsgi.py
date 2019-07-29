import os
import sys

sys.path.append('/app/meru_os')
sys.path.append('/app/meru_os/oscab_env')

from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "outstation.settings.production")

_application  = get_wsgi_application()

def application(environ, start_response):
    script_name = getattr(settings, 'X_SCRIPT_NAME', None)
    if script_name:
        environ['SCRIPT_NAME'] = script_name
        path_info = environ['PATH_INFO']
        if path_info.startswith(script_name):
            environ['PATH_INFO'] = path_info[len(script_name):]

    scheme = environ.get('HTTP_X_SCHEME', '')

    if scheme:
        environ['wsgi.url_scheme'] = scheme

    return _application(environ, start_response)
