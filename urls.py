from django.conf.urls import url

# We can't import the theme module directly because it has a hyphen in its name. This works well.
import importlib
theme_views = importlib.import_module('presupuesto-barcelona.views')

# We can define additional URLs applicable only to the theme. These will get added
# to the project URL patterns list.
EXTRA_URLS = (
    url(r'^accesibilidad$', theme_views.accesibilidad, name='accesibilidad'),
    url(r'^aviso_legal$', theme_views.aviso_legal, name='aviso_legal')
)
