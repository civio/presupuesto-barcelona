# -*- coding: UTF-8 -*-

from coffin.shortcuts import render_to_response
from budget_app.views.helpers import *


def accesibilidad(request):
    c = get_context(request, css_class='body-articles', title=u'Accesibilidad')

    return render_to_response('legal_pages/accesibilidad.html', c)

def aviso_legal(request):
    c = get_context(request, css_class='body-articles', title=u'Aviso legal')

    return render_to_response('legal_pages/aviso_legal.html', c)
