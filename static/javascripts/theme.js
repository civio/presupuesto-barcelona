// Custom for descriptions in some programmes
$(document).ready(function(){

  var descriptions = {
    '/es/politicas/16': 'En 2014 y años anteriores el programa 1623 Tratamiento de residuos integra tanto el tratamiento como la gestión de residuos. A partir del 2015 el tratamiento y la gestión de residuos se separen en 2 programas.',
    '/ca/politicas/16': 'Al 2014 i anys anteriors el programa 1623 Tractament de residus comprèn tant el tractament com la gestió de residus. A partir del 2015 el tractament i la gestió de residus se separen en 2 programes.',
    '/es/politicas/23': 'En el programa 2315 Servicios sociales básicos y en el ejercicio 2013, parte de los recursos relativos a la atención social y limpieza del hogar (SAD) estaban imputados en el subprograma servicios sociales básicos.',
    '/ca/politicas/23': "En el programa 2315 Serveis socials bàsics i en els exercicis 2012 i 2013, part dels recursos relatius a l'atenció social i neteja de la llar (SAD) es trobaven imputats al subprograma serveis socials bàsics.",
    '/es/politicas/32': 'En el 2015, a raíz de la orden ministerial que modifica la estructura presupuestaria de las corporaciones locales, los recursos relativos al apoyo obligatorio a los centros educativos se imputa a los programes relativos al funcionamiento de los centros de educación infantil y primaria y a los de secundaria y FP. En el 2015 los recursos del programa 3253 otras enseñanzas se reparten en dos nuevos programas, el programa 3233 funcionamiento de los centros de educación especial y el programa 3283 de formación de adultos.',
    '/ca/politicas/32': "En el 2015, arran l'ordre ministerial que modifica l'estructura pressupostària dels ens locals, els recursos relatius al suport obligatori als centres educatius s'imputa als programes relatius al funcionament dels centres d'educació infantil i primària i als de secundària i FP. En el 2015 els recursos del programa 3253 d'altres ensenyaments es reparteixen en dos nous programes, el programa 3233 de funcionament dels centres d'educació especial i el programa 3283 de formació d'adults.",
    '/es/politicas/34': 'En 2013 los recursos relativos a instalaciones deportivas se imputaban dentro del programa de gestión y promoción del deporte.',
    '/ca/politicas/34': "Al 2013 els recursos relatius a instal·lacions esportives es trobaven dins del programa de gestió i promoció de l'esport.",
    '/es/politicas/43': "Dentro del programa 4331 apoyo a la empresa, la emprendeduría y la ocupación están imputados los gastos relativos al plan de rescate social.",
    '/ca/politicas/43': "Dins del programa 4331 de suport a l’ocupació i l’empresa hi són imputades les despeses relatives al pla de rescat social.",
    '/es/politicas/44': "A partir del 2014 en el programa 4412 otros transportes de viajeros, se imputan en el presupuesto del Ayuntamiento todos los gastos (así como también sus ingresos) relativos al servicio del Bicing, en lugar de imputarse los gastos relativos a la transferencia para la entidad BSM con el fin de mantener el equilibrio económico del servicio.",
    '/ca/politicas/44': "A partir del 2014 en el programa 4412 d'altres transports de viatgers, s'imputen al pressupost de l'Ajuntament totes les despeses (així com també els ingressos) relatives al servei del Bicing, enlloc d'imputar-se les despeses relatives a la transferència per a l'entitat BSM per tal de mantenir l'equilibri econòmic del servei.",
  };

  var description = descriptions[ window.location.pathname.substring(0,window.location.pathname.lastIndexOf('/')) ];

  if (description) {
    $('.policies .policies-content .policies-chart').append( '<p class="policy-description">'+description+'</p>' );
  }
});