# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url
from django.conf.urls.i18n import i18n_patterns

MAIN_ENTITY_LEVEL = 'municipio'
MAIN_ENTITY_NAME = 'Barcelona'

BUDGET_LOADER = 'BarcelonaBudgetLoader'
PAYMENTS_LOADER = 'BarcelonaPaymentsLoader'

# Number of programmes to feature in home page. Default: 3
NUMBER_OF_FEATURED_PROGRAMMES = 1

# List of programmes to feature
FEATURED_PROGRAMMES = ['1532', '2313', '3291', '3321', '3371', '4411', '1711', '1631', '1321', '4314']

OVERVIEW_INCOME_NODES = [
                          {
                            'label.es': 'Impuesto sobre bienes inmuebles (IBI)',
                            'label.en': 'Property tax (IBI)',
                            'label.ca': 'Impost sobre béns immobles (IBI)',
                            'nodes': [['11', '113'], ['11', '114']],
                            'link_id': '11'
                          },
                          {
                            'label.es': 'Otros impuestos locales propios (plusvalía, IAE, circulación e ICIO)',
                            'label.en': 'Other own local taxes (capital gains, economic activity tax, road tax and construction tax)',
                            'label.ca': 'Resta d\'impostos locals propis (plusvàlua, IAE, circulació i ICIO)',
                            'nodes': [['11', '115'], ['11', '116'], '13', '29']
                          },
                          {
                            'label.es': 'Impuestos cedidos (IRPF, IVA y especiales)',
                            'label.en': 'Assigned taxes (income tax, VAT and special taxes)',
                            'label.ca': 'Impostos cedits (IRPF, IVA i especials)',
                            'nodes': ['10', '21', '22']
                          },
                          {
                            'label.es': 'Tasas, precios públicos y otros',
                            'label.en': 'Municipal and public-sector charges and other revenue',
                            'label.ca': 'Taxes, preus públics i altres',
                            'nodes': ['30', '32', '33', '34', '35', '36', '38', '39']
                          },
                          {
                            'label.es': 'Transferencias corrientes del Estado',
                            'label.en': 'Current transfers from Spanish central government',
                            'label.ca': 'Transferències corrents de l\'Estat',
                            'nodes': '42',
                            'link_id': '42'
                          },
                          {
                            'label.es': 'Transferencias corrientes de comunidades autónomas, entes locales y otros',
                            'label.en': 'Current transfers from regional governments, local authorities and others',
                            'label.ca': 'Transferències corrents de comunitats autònomes, ens locals i altres',
                            'nodes': ['41', '44', '45', '46', '47', '48', '49']
                          },
                          {
                            'label.es': 'Rendimientos patrimoniales',
                            'label.en': 'Equity returns',
                            'label.ca': 'Rendiments patrimonials',
                            'nodes': ['50', '52', '53', '54', '55']
                          },
                          {
                            'label.es': 'Ingresos de capital',
                            'label.en': 'Capital income',
                            'label.ca': 'Ingressos de capital',
                            'nodes': ['60', '61', '68', '75', '79']
                          },
                          {
                            'label.es': 'Ingresos financieros',
                            'label.en': 'Financial income',
                            'label.ca': 'Ingressos financers',
                            'nodes': ['84', '90', '94']
                          }
                        ]
OVERVIEW_EXPENSE_NODES =  [
                            {
                              'label.es': 'Seguridad y movilidad ciudadana',
                              'label.en': 'Security and citizen mobility',
                              'label.ca': 'Seguretat i mobilitat ciutadana',
                              'nodes': '13'
                            },
                            {
                              'label.es': 'Vivienda y urbanismo',
                              'label.en': 'Housing and urban planning',
                              'label.ca': 'Habitatge i urbanisme',
                              'nodes': ['15', '45'],
                              'link_id': '15'
                            },
                            {
                              'label.es': 'Servicios urbanos y medio ambiente',
                              'label.en': 'Urban services and environment',
                              'label.ca': 'Serveis urbans i medi ambient',
                              'nodes': ['16', '17'],
                              'link_id': '16'
                            },
                            {
                              'label.es': 'Servicios sociales y salud',
                              'label.en': 'Social services and health',
                              'label.ca': 'Serveis socials i salut',
                              'nodes': ['23', '31'],
                              'link_id': '23'
                            },
                            {
                              'label.es': 'Educación',
                              'label.en': 'Education',
                              'label.ca': 'Educació',
                              'nodes': '32'
                            },
                            {
                              'label.es': 'Cultura',
                              'label.en': 'Culture',
                              'label.ca': 'Cultura',
                              'nodes': '33'
                            },
                            {
                              'label.es': 'Deporte',
                              'label.en': 'Sport',
                              'label.ca': 'Esports',
                              'nodes': '34'
                            },
                            {
                              'label.es': 'Promoción económica y empleo',
                              'label.en': 'Economic promotion and employment',
                              'label.ca': 'Promoció econòmica i ocupació',
                              'nodes': ['43', ['49', '4931']],
                              'link_id': '43'
                            },
                            {
                              'label.es': 'Transporte público',
                              'label.en': 'Public transport',
                              'label.ca': 'Transport públic',
                              'nodes': '44'
                            },
                            {
                              'label.es': 'Órganos de gobierno',
                              'label.en': 'Government bodies',
                              'label.ca': 'Òrgans de govern',
                              'nodes': '91'
                            },
                            {
                              'label.es': 'Transferencias a otras administraciones',
                              'label.en': 'Transfers to other public authorities',
                              'label.ca': 'Transferències a altres administracions',
                              'nodes': '94'
                            },
                            {
                              'label.es': 'Servicios de carácter general y administración',
                              'label.en': 'General services and administration',
                              'label.ca': 'Serveis de caràcter general i administració',
                              'nodes': ['21', '92', '93', ['49', '4911']],
                              'link_id': '92'
                            },
                            {
                              'label.es': 'Deuda',
                              'label.en': 'Public debt',
                              'label.ca': 'Deute',
                              'nodes': '01'
                            }
                          ]

# How much padding between Sankey nodes. Default: 10 (Optional)
# Note: higher values will result in a more 'curvy accordion'.
OVERVIEW_NODE_PADDING = 15

# How aggresive should the Sankey diagram reorder the nodes. Default: 0.79 (Optional)
# Note: 0.5 usually leaves nodes ordered as defined. 0.95 sorts by size (decreasing).
OVERVIEW_RELAX_FACTOR = 0.5

# Does the data includes a fifth functional classification level, subprogrammes?. Default: False
USE_SUBPROGRAMMES = True

# Show Payments section in menu & home options. Default: False.
SHOW_PAYMENTS           = True

# Configure 'by area' payment breakdown. Default: ['area', 'payee', 'description']
PAYMENTS_BREAKDOWN_BY_AREA = ['area', 'programme', 'payee', 'description']

# Configure 'by payee' payment breakdown. Default: ['payee', 'area', 'description']
# PAYMENTS_BREAKDOWN_BY_PAYEE = ['payee', 'area', 'description']

# Define if payments year slider is a range (True) or a single year (False). Default: True
PAYMENTS_YEAR_RANGE = False

# Show Tax Receipt section in menu & home options. Default: False.
# SHOW_TAX_RECEIPT        = False

# Show Counties & Towns links in Policies section in menu & home options. Default: False.
# SHOW_COUNTIES_AND_TOWNS = False

# Show an extra tab with institutional breakdown. Default: True.
SHOW_INSTITUTIONAL_TAB  = True

# Show an extra tab with funding breakdown (only applicable to some budgets). Default: False.
# SHOW_FUNDING_TAB = False

# Adjust inflation in amounts in Overview page. Default: True
ADJUST_INFLATION_IN_OVERVIEW = False

# Show Subtotals panel in Overview. Default: False
SHOW_OVERVIEW_SUBTOTALS = True

# Calculate budget indicators (True), or show/hide the ones hardcoded in HTML (False). Default: True.
CALCULATE_BUDGET_INDICATORS = False

# Show an extra column with actual revenues/expenses. Default: True.
# Warning: the execution data still gets shown in the summary chart and in downloads.
#SHOW_ACTUAL = True

# Include financial income/expenditures in overview and global policy breakdowns. Default: False.
INCLUDE_FINANCIAL_CHAPTERS_IN_BREAKDOWNS = True

# Search in entity names. Default: True.
SEARCH_ENTITIES = False

# Supported languages. Default: ('es', 'Castellano')
LANGUAGES = (
  ('ca', 'Catal&agrave;'),
  ('es', 'Castellano'),
  ('en', 'English'),
)

# Setup Data Source Budget link
DATA_SOURCE_BUDGET      = 'http://governobert.bcn.cat/estrategiaifinances/es/i-pressupost'

# Setup Data Source Population link
DATA_SOURCE_POPULATION  = 'http://www.ine.es/jaxiT3/Tabla.htm?t=2861'

# Setup Data Source Inflation link
DATA_SOURCE_INFLATION   = 'http://www.ine.es/jaxiT3/Tabla.htm?t=10019&L=0'

# Setup Main Entity Web Url
MAIN_ENTITY_WEB_URL     = 'http://ajuntament.barcelona.cat/es/'

# Setup Main Entity Legal Url (if empty we hide the link)
#MAIN_ENTITY_LEGAL_URL   = 'http://ajuntament.barcelona.cat/es/aviso-legal'

# External URL for Cookies Policy (if empty we use out template page/cookies.html)
COOKIES_URL             = 'http://www.barcelona.cat/es/cookies.html'

# Allow overriding of default treemap color scheme
COLOR_SCALE = [ '#1f77b4', '#ee6f00', '#2ca02c', '#d62728', '#8350b2', '#8c564b', '#d944ac', '#d74a54', '#8c8c19', '#118996' ]

# We can define additional URLs applicable only to the theme. These will get added
# to the project URL patterns list.
EXTRA_URLS = i18n_patterns('presupuesto-barcelona.views',
    url(r'^accesibilidad$', 'accesibilidad'),
    url(r'^aviso_legal$', 'aviso_legal')
)

# Make environment setting available to URL monkey-patch in __init__.py
if ENV.get('USE_PRODUCTION_URLS') == True:
  USE_PRODUCTION_URLS = True
