# This is an example settings/local.py file.
# These settings can override what's in settings/base.py


# On a production site, you'd want to import the
# appropriate site settings like this:
#
# from .sites.dev.settings_base import *
from . import base

# This is for development:
INSTALLED_APPS = base.INSTALLED_APPS + (
    'django_nose',
)

# Recipients of traceback emails and other notifications.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = True

# Make this unique, and don't share it with anybody.  It cannot be blank.
SECRET_KEY = 'asdasdas'

HAWK_CREDENTIALS = base.HAWK_CREDENTIALS
# Set these to long random strings.
HAWK_CREDENTIALS['marketplace-signing']['key'] = ''
