# -*- coding: UTF-8 -*-

from django.utils.translation import ugettext as _

# Set metadata fields before response is returned.
# Themes can override this method if needed (e.g. see #469)
def _set_meta_fields(c):
    # Not ideal, but the body CSS class name is the best proxy to know
    # which section we're dealing with. We remove the prefix for clarity.
    section = c['page_css_class'].replace('body-', '')

    # Some sections require some manipulation, though, as they have multiple css classes
    if 'subprogrammes' in section:
        section = 'subprogrammes'
    elif 'programmes' in section:
        section = 'programmes'
    elif 'policies' in section:
        section = 'policies'

    # Based on the current section, use different meta tags, per client request.
    # Some of the sections have fixed texts, so we rely on the i18n framework
    # to simplify the code.
    if section in ['welcome', 'summary', 'entities', 'payments', 'glossary']:
        c['meta_title'] = _("meta_%s_title" % (section))
        c['meta_description'] = _("meta_%s_description" % (section))
        c['meta_og_title'] = _("meta_%s_og_title" % (section))
        c['meta_og_description'] = _("meta_%s_og_description" % (section))

    elif section in ['policies', 'programmes', 'subprogrammes']:
        c['meta_title'] = (_("meta_%s_title" % (section)) % (c['name']))
        c['meta_description'] = (_("meta_%s_description" % (section)) % (c['name']))
        c['meta_og_title'] = (_("meta_%s_og_title" % (section)) % (c['name']))
        c['meta_og_description'] = (_("meta_%s_og_description" % (section)) % (c['name']))

    else:
        c['meta_title'] = _(u'Presupuestos del Gobierno de Aragón')
        if c['title_prefix']:
            c['meta_title'] = c['title_prefix'] + ' - ' + c['meta_title']

        c['meta_description'] = _(u'Información presupuestaria del Gobierno de Aragón')

        c['meta_og_title'] = c['meta_title']
        c['meta_og_description'] = c['meta_description']

    # The following remain as in the core
    c['meta_keywords'] = _('presupuestos, gastos, ingresos') + ', ' + _(u'Gobierno de Aragón')
    # Note that Barcelona requested to use AddThis, so we can't control the tweet text
    c['meta_tweet_text'] = c['meta_title']
