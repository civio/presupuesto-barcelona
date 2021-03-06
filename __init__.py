# Adapted from https://djangosnippets.org/snippets/1467/
from django.core import urlresolvers
from django.conf import settings

def reverse_decorator(func):
    def inner(*args, **kwargs):
        abs_path = func(*args,**kwargs)

        # In production, rewrite URLs to use the prefixes provided by the client
        if hasattr(settings, 'USE_PRODUCTION_URLS') and settings.USE_PRODUCTION_URLS == True:
            if abs_path.startswith('/ca/'):
                abs_path = '/estrategiaifinances/pressupostobert/ca' + abs_path[3:]
            elif abs_path.startswith('/en/'):
                abs_path = '/estrategiaifinances/pressupostobert/en' + abs_path[3:]
            elif abs_path.startswith('/es/'):
                abs_path = '/estrategiaifinances/pressupostobert/es' + abs_path[3:]

        return abs_path
    return inner
urlresolvers.reverse = reverse_decorator(urlresolvers.reverse)


# Override metadata information from core
import budget_app.views.helpers as core_helpers
from views.helpers import _set_meta_fields

core_helpers._set_meta_fields = _set_meta_fields
