// Theme custom js methods
$(document).ready(function(){

  // Custom for descriptions in some programmes
  var addCustomDescriptions = function(){
    var linkTextES = 'Consulta las descripciones de los programas y los indicadores de gestión';
    var linkTextCA = 'Consulta les descripcions dels programes i els indicadors de gestió';
    var linkTextEN = 'Consult the program expenditure and performance indicator descriptions';

    var descriptions = {
      '/estrategiaifinances/pressupostobert/es/politicas/01': {
        'text': '',
        'link': 'http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-gasto-de-deuda-p%C3%Bablica',
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/ca/politicas/01': {
        'text': '',
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-deute-p%C3%Bablic',
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/en/politicas/01': {
        'text': '',
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-deute-p%C3%Bablic',
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/ca/politicas/13': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-seguretat-i-mobilitat",
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/es/politicas/13': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-despesa-de-seguretat-i-mobilitat",
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/en/politicas/13': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-seguretat-i-mobilitat",
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/ca/politicas/15': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-dhabitatge-i-urbanisme",
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/es/politicas/15': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-gasto-de-bienestar-comunitario-servicios-urbanos",
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/en/politicas/15': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-dhabitatge-i-urbanisme",
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/es/politicas/16': {
        'text': 'En 2014 y años anteriores el programa 1623 de tratamiento de residuos integra tanto el tratamiento como la gestión de residuos. A partir del 2015 el tratamiento y la gestión de residuos se separen en 2 programas.',
        'link': 'http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-gasto-de-bienestar-comunitario-servicios-urbanos',
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/ca/politicas/16': {
        'text': 'Al 2014 i anys anteriors el programa 1623 de tractament de residus comprèn tant el tractament com la gestió de residus. A partir del 2015 el tractament i la gestió de residus se separen en 2 programes.',
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-benestar-comunitari-serveis-urbans',
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/en/politicas/16': {
        'text': 'In 2014 and prior years, the 1623 waste treatment program integrates both waste treatment and management. As of 2015, treatment and waste management are separated into 2 programs.',
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-benestar-comunitari-serveis-urbans',
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/ca/politicas/17': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-medi-ambient",
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/es/politicas/17': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-gasto-de-medio-ambiente",
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/en/politicas/17': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-medi-ambient",
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/ca/politicas/21': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-pensions",
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/es/politicas/21': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-despesa-de-pensions",
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/en/politicas/21': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-pensions",
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/es/politicas/23': {
        'text': 'En el programa 2315 de servicios sociales básicos y en los ejercicios 2012 y 2013, parte de los recursos relativos a la atención social y limpieza del hogar (SAD) estaban imputados en el subprograma servicios sociales básicos.',
        'link': 'http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-gasto-de-servicios-sociales-y-promoci%C3%B3n-social',
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/ca/politicas/23': {
        'text': "En el programa 2315 de serveis socials bàsics i en els exercicis 2012 i 2013, part dels recursos relatius a l'atenció social i neteja de la llar (SAD) es trobaven imputats al subprograma serveis socials bàsics.",
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-serveis-socials-i-promoci%C3%B3-social',
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/en/politicas/23': {
        'text': "In the 2315 basic social services program and in the financial years 2012 and 2013, part of the resources related to social care and cleaning of the home (SAD) were charged to the subprogram basic social services.",
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-serveis-socials-i-promoci%C3%B3-social',
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/ca/politicas/31': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-salut",
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/es/politicas/31': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-despesa-de-salut",
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/en/politicas/31': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-salut",
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/es/politicas/32': {
        'text': 'En el 2015, a raíz de la orden ministerial que modifica la estructura presupuestaria de las corporaciones locales, los recursos relativos al apoyo obligatorio a los centros educativos se imputa a los programes relativos al funcionamiento de los centros de educación infantil y primaria y a los de secundaria y FP. En el 2015 los recursos del programa 3253 de otras enseñanzas se reparten en dos nuevos programas, el programa 3233 de funcionamiento de los centros de educación especial y el programa 3283 de formación de adultos.',
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-deducaci%C3%B3',
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/ca/politicas/32': {
        'text': "En el 2015, arran l'ordre ministerial que modifica l'estructura pressupostària dels ens locals, els recursos relatius al suport obligatori als centres educatius s'imputa als programes relatius al funcionament dels centres d'educació infantil i primària i als de secundària i FP. En el 2015 els recursos del programa 3253 d'altres ensenyaments es reparteixen en dos nous programes, el programa 3233 de funcionament dels centres d'educació especial i el programa 3283 de formació d'adults.",
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-deducaci%C3%B3',
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/en/politicas/32': {
        'text': "In 2015, as a result of the ministerial order that modifies the budgetary structure of local corporations, the resources related to mandatory support to education centers are charged to the pre-school and primary school centres functioning and high school and vocational training centres functioning programs. In 2015 the 3253 other education program resources are divided into two new programs, the 3233 running special-education schools program and the 3283 adult education and training program.",
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-deducaci%C3%B3',
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/ca/politicas/33': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-cultura",
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/es/politicas/33': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-despesa-de-cultura",
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/en/politicas/33': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-cultura",
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/es/politicas/34': {
        'text': 'En 2013 los recursos relativos a instalaciones deportivas se imputaban dentro del programa de gestión y promoción del deporte.',
        'link': 'http://governobert.bcn.cat/estrategiaifinances/es/politica-de-despesa-desports',
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/ca/politicas/34': {
        'text': "Al 2013 els recursos relatius a instal·lacions esportives es trobaven dins del programa de gestió i promoció de l'esport.",
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/politica-de-despesa-desports',
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/en/politicas/34': {
        'text': "In 2013, the resources related to sports facilities were charged to the managing and promoting sport program.",
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/politica-de-despesa-desports',
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/es/politicas/43': {
        'text': "Dentro del programa 4331 de apoyo a la empresa, la emprendeduría y la ocupación están imputados los gastos relativos al plan de rescate social.",
        'link': 'http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-despesa-de-promoci%C3%B3-econ%C3%B2mica-i-ocupaci%C3%B3',
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/ca/politicas/43': {
        'text': "Dins del programa 4331 de suport a l’ocupació i l’empresa hi són imputades les despeses relatives al pla de rescat social.",
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-promoci%C3%B3-econ%C3%B2mica-i-ocupaci%C3%B3',
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/en/politicas/43': {
        'text': "Expenses related to the social rescue plan are charged to the 4331 employment and business support program.",
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-promoci%C3%B3-econ%C3%B2mica-i-ocupaci%C3%B3',
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/es/politicas/44': {
        'text': "A partir del 2014 en el programa 4412 otros transportes de viajeros, se imputan en el presupuesto del Ayuntamiento todos los gastos (así como también sus ingresos) relativos al servicio del Bicing, en lugar de imputarse los gastos relativos a la transferencia para la entidad BSM con el fin de mantener el equilibrio económico del servicio.",
        'link': 'http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-despesa-de-transport-p%C3%Bablic',
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/ca/politicas/44': {
        'text': "A partir del 2014 en el programa 4412 d'altres transports de viatgers, s'imputen al pressupost de l'Ajuntament totes les despeses (així com també els ingressos) relatives al servei del Bicing, enlloc d'imputar-se les despeses relatives a la transferència per a l'entitat BSM per tal de mantenir l'equilibri econòmic del servei.",
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-transport-p%C3%Bablic',
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/en/politicas/44': {
        'text': "As of 2014 all the expenses (as well as the income) related to the Bicing service are charged to the 4412 other passenger transport program in the City Council budget, instead of reflecting the expenses related to the transfer for the BSM entity, in order to maintain the economic balance of the service.",
        'link': 'http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-transport-p%C3%Bablic',
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/ca/politicas/49': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-daltres-actuacions-de-car%C3%A0cter-econ%C3%B2mic",
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/es/politicas/49': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-despesa-daltres-actuacions-de-car%C3%A0cter-econ%C3%B2mic",
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/en/politicas/49': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-daltres-actuacions-de-car%C3%A0cter-econ%C3%B2mic",
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/ca/politicas/91': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-d%C3%B2rgans-de-govern",
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/es/politicas/91': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-despesa-d%C3%B2rgans-de-govern",
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/en/politicas/91': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-d%C3%B2rgans-de-govern",
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/ca/politicas/92': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-serveis-de-car%C3%A0cter-general",
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/es/politicas/92': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-despesa-de-serveis-de-car%C3%A0cter-general",
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/en/politicas/92': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-serveis-de-car%C3%A0cter-general",
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/ca/politicas/93': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-dadministraci%C3%B3-financera-i-tribut%C3%A0ria",
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/es/politicas/93': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-despesa-dadministraci%C3%B3-financera-i-tribut%C3%A0ria",
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/en/politicas/93': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-dadministraci%C3%B3-financera-i-tribut%C3%A0ria",
        'linkText': linkTextEN
      },

      '/estrategiaifinances/pressupostobert/ca/politicas/94': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-transfer%C3%A8ncies-altres-administracions",
        'linkText': linkTextCA
      },
      '/estrategiaifinances/pressupostobert/es/politicas/94': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/es/pol%C3%ADtica-de-despesa-de-transfer%C3%A8ncies-altres-administracions",
        'linkText': linkTextES
      },
      '/estrategiaifinances/pressupostobert/en/politicas/94': {
        'text': '',
        'link': "http://governobert.bcn.cat/estrategiaifinances/ca/pol%C3%ADtica-de-despesa-de-transfer%C3%A8ncies-altres-administracions",
        'linkText': linkTextEN
      }
    };

    var description = descriptions[ window.location.pathname.substring(0,window.location.pathname.lastIndexOf('/')) ];

    if (description) {
      $('.policies .policies-content .policies-chart').append( '<div class="policy-description"><p>'+description.text+'</p><p><a href="'+description.link+'" target="_blank" title="'+description.linkText+'">'+description.linkText+'</a>'+'</p></div>' );
    }
  };

  var addYearSelectorCustomLabels = function(){
    var lang = $('html').attr('lang')
    var extended = {
      'es': 'prorrogado',
      'ca': 'prorrogat',
      'en': 'extended',
    };
    var extendedWithNote = {
      'es': 'prorrogado, ver nota',
      'ca': 'prorrogat, veure nota',
      'en': 'extended, see note',
    };
    var pendingApproval = {
      'es': 'pendiente aprobación',
      'ca': 'pendent aprovació',
      'en': 'pending approval',
    };
    var yearLabels = {
      '2013': extended,
      '2019': extendedWithNote
    }

    $('.data-controllers .layout-slider .slider .slider-tick-label').each(function(){
      var year = $(this).html();
      var label = yearLabels[year]

      if (typeof(label) === 'undefined') {
        return
      }

      $(this).html(year + '<br/><small><i> ('+ label[lang] +')</i></small>');
    });
  };

  var showInvoicesNote = function(){
    if ( $('body').hasClass('body-payments') )
      $('.data-sources li.hidden').removeClass('hidden');
  };

  var addChartsAlert = function(selector){
    var str = {
      'es': 'Desplaza el cursor sobre la infografía para ver el detalle',
      'ca': 'Desplaça el cursor sobre la infografia per a veure el detall',
      'en': 'Hover over the infographic to see the details'
    };
    var cont = $(selector);
    if( cont.size() > 0 ){
      cont.prepend('<div class="alert alert-success"><i class="glyphicon glyphicon-hand-up"></i> '+str[ $('html').attr('lang') ]+'</div>');
    }
  };

  var moveDataControllersOnTop  = function(){
    $('.policies-content .data-controllers').detach().insertBefore('.policies-chart');
    $('.budget-viz .data-controllers').detach().insertBefore('.sankey-container');
  };


  addChartsAlert('.policies-chart');
  addChartsAlert('.sankey-container');
  addCustomDescriptions();
  addYearSelectorCustomLabels();
  showInvoicesNote();
  moveDataControllersOnTop();
});

// Avoid space before percentage sign
window.percentage_sign_suffix = '%';
