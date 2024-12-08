import re
import sys

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage


def is_managed() -> bool:
    """
    Check if a Django project is being managed with ``manage.py`` or
    ``django-admin`` scripts

    :return: Check result
    :rtype: bool
    """
    return any(re.search('manage.py|django-admin|django', item) is not None for item in sys.argv)


# Default TinyMCE 4 configuration
DEFAULT = {
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': 'link image preview codesample contextmenu table code lists',
    'toolbar1': 'formatselect | bold italic underline | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | table | link image | codesample | preview code',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'inline': False,
    'statusbar': True,
    'width': 'auto',
    'height': 360,
}

# Use tinymce4 built-in spellchecker service
USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)

# TinyMCE 4 configuration
if USE_SPELLCHECKER:
    DEFAULT['plugins'] += ' spellchecker'
    DEFAULT['toolbar1'] += ' | spellchecker'
CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG', DEFAULT)

# TinyMCE 4 JavaScript code
JS_URL = getattr(settings, 'TINYMCE_JS_URL', None)
if JS_URL is None:
    # Ugly hack that allows to run management commands with ManifestStaticFilesStorage
    _orig_debug = settings.DEBUG
    if is_managed():
        settings.DEBUG = True
    JS_URL = staticfiles_storage.url('tinymce/js/tinymce/tinymce.min.js')
    settings.DEBUG = _orig_debug

# Additional JS files for TinyMCE (e.g. custom plugins)
ADDIONAL_JS_URLS = getattr(settings, 'TINYMCE_ADDITIONAL_JS_URLS', None)

# TinyMCE 4 calback JavaScript functions
CALLBACKS = getattr(settings, 'TINYMCE_CALLBACKS', {})

"""
Additional CSS styles for TinyMCE 4. The default CSS is used to fix TinyMCE 4 position in Django Admin.
"""
CSS_URL = getattr(settings, 'TINYMCE_CSS_URL', None)

# Enable integration with `django-filebrowser-no-grappelli`
USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER', 'filebrowser' in settings.INSTALLED_APPS)

DISABLE_MARGIN_FIX = getattr(settings, 'TINYMCE_DISABLE_MARGIN_FIX', False)
