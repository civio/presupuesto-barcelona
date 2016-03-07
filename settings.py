# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url

MAIN_ENTITY_LEVEL = 'municipio'
MAIN_ENTITY_NAME = 'Barcelona'

BUDGET_LOADER = 'BarcelonaBudgetLoader'
PAYMENTS_LOADER = 'BarcelonaPaymentsLoader'

FEATURED_PROGRAMMES = ['1532', '2313', '3291', '3321', '3371', '4411', '1711', '1631', '1321', '4314']

OVERVIEW_INCOME_NODES = [
                          {
                            'label.es': 'Impuesto sobre bienes inmuebles (IBI)',
                            'label.en': 'Property tax (IBI)',
                            'label.ca': 'Impost sobre béns immobles (IBI)',
                            'nodes': [['11', '113'], ['11', '114']]
                          },
                          {
                            'label.es': 'Otros impuestos locales propios (plusvalía, IAE, circulación y ICIO)',
                            'label.en': 'Other own local taxes (capital gains, IAE, road tax and ICIO)',
                            'label.ca': 'Resta d\'impostos locals propis (plusvàlua, IAE, circulació y ICIO)',
                            'nodes': [['11', '115'], ['11', '116'], '13', '29']
                          },
                          {
                            'label.es': 'Impuestos cedidos (IRPF, VAT y especiales)',
                            'label.en': 'Transferred taxes (income tax, VAT and excises)',
                            'label.ca': 'Impostos cedits (IRPF, IVA i especials)',
                            'nodes': ['10', '21', '22']
                          },
                          {
                            'label.es': 'Tasas, precios públicos y otros',
                            'label.en': 'Fees, sales and other revenues',
                            'label.ca': 'Taxes, preus públics i altres',
                            'nodes': ['30', '32', '33', '34', '35', '36', '38', '39']
                          },
                          {
                            'label.es': 'Transferencias corrientes del estado',
                            'label.en': 'Current transfers from Spanish central government',
                            'label.ca': 'Transferències corrents de l\'estat',
                            'nodes': '42'
                          },
                          {
                            'label.es': 'Transferencias corrientes de comunidades autónomas, entes locales y otros',
                            'label.en': 'Current transfers from regions, local authorities and others',
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
                            'label.en': 'Capital inflows',
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
                              'label.es': 'Deuda',
                              'label.en': 'Public debt',
                              'label.ca': 'Deute',
                              'nodes': '01'
                            },
                            {
                              'label.es': 'Seguridad y mobilidad ciudadana',
                              'label.en': 'Security and citizen mobility',
                              'label.ca': 'Seguretat i mobilitat ciutadana',
                              'nodes': '13'
                            },
                            {
                              'label.es': 'Vivienda y urbanismo',
                              'label.en': 'Housing and urban planning',
                              'label.ca': 'Habitatge i urbanisme',
                              'nodes': ['15', '45']
                            },
                            {
                              'label.es': 'Servicios urbanos y medio ambiente',
                              'label.en': 'Urban services and environment',
                              'label.ca': 'Serveis urbans i medi ambient',
                              'nodes': ['16', '17']
                            },
                            {
                              'label.es': 'Servicios sociales y salud',
                              'label.en': 'Social services and health',
                              'label.ca': 'Serveis socials i salut',
                              'nodes': ['23', '31']
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
                              'nodes': ['43', ['49', '4931']]
                            },
                            {
                              'label.es': 'Transporte público',
                              'label.en': 'Public transportation',
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
                              'label.es': 'Transferencias a otras administraciónes',
                              'label.en': 'Transfers to other public administrations',
                              'label.ca': 'Transferències a altres administracions',
                              'nodes': '94'
                            },
                            {
                              'label.es': 'Servicios de carácter general y administración',
                              'label.en': 'General services and administration',
                              'label.ca': 'Serveis de caràcter general i administració',
                              'nodes': ['21', '92', '93', ['49', '4911']]
                            }
                          ]

# How aggresive should the Sankey diagram reorder the nodes. Default: 0.79 (Optional)
# Note: 0.5 usually leaves nodes ordered as defined. 0.95 sorts by size (decreasing).
OVERVIEW_RELAX_FACTOR = 0.5

# Show Payments section in menu & home options. Default: False.
SHOW_PAYMENTS           = False

# Configure 'by area' payment breakdown. Default: ['area', 'payee', 'description']
PAYMENTS_BREAKDOWN_BY_AREA = ['area', 'programme', 'payee', 'description']

# Configure 'by payee' payment breakdown. Default: ['payee', 'area', 'description']
# PAYMENTS_BREAKDOWN_BY_PAYEE = ['payee', 'area', 'description']

# Show Tax Receipt section in menu & home options. Default: False.
# SHOW_TAX_RECEIPT        = False

# Show Counties & Towns links in Policies section in menu & home options. Default: False.
# SHOW_COUNTIES_AND_TOWNS = False

# Show an extra tab with institutional breakdown. Default: True.
SHOW_INSTITUTIONAL_TAB  = True

# Show an extra tab with funding breakdown (only applicable to some budgets). Default: False.
# SHOW_FUNDING_TAB = False

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
MAIN_ENTITY_LEGAL_URL   = 'http://ajuntament.barcelona.cat/es/aviso-legal'

# External URL for Cookies Policy (if empty we use out template page/cookies.html)
COOKIES_URL             = 'http://www.barcelona.cat/es/cookies.html'

# Allow overriding of default treemap color scheme
COLOR_SCALE = [ '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#e7969c', '#bcbd22', '#17becf' ]
