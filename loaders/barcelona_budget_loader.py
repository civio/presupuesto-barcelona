# -*- coding: UTF-8 -*-
from budget_app.models import *
from budget_app.loaders import SimpleBudgetLoader
from decimal import *
import csv
import os
import re

class BarcelonaBudgetLoader(SimpleBudgetLoader):

    # An artifact of the in2csv conversion of the original XLS files is a trailing '.0', which we remove here
    def clean(self, s):
        return s.split('.')[0]

    def parse_item(self, filename, line):
        # Programme codes have changed in 2015, due to new laws. Since the application expects a code-programme
        # mapping to be constant over time, we are forced to amend budget data prior to 2015.
        # See https://github.com/dcabo/presupuestos-aragon/wiki/La-clasificaci%C3%B3n-funcional-en-las-Entidades-Locales
        programme_mapping = {
        }

        is_expense = (filename.find('gastos.csv')!=-1)
        is_actual = (filename.find('/ejecucion_')!=-1)
        if is_expense:
            fc_code = self.clean(line[2])

            # For years before 2015 we check whether we need to amend the programme code
            year = re.search('municipio/(\d+)/', filename).group(1)
            if int(year) < 2015:
                fc_code = programme_mapping.get(fc_code, fc_code)

            # The budget data we have for 2016 doesn't (yet) have amended expense figures,
            # so in that case we use the initial budget
            budget_column = 4 if int(year)==2016 else 5

            return {
                'is_expense': True,
                'is_actual': is_actual,
                'fc_code': fc_code,
                'ec_code': self.clean(line[0])[:-2],
                'ic_code': self.clean(line[1])[1:],
                'item_number': self.clean(line[0])[-2:],    # Last two digits
                'description': line[3],
                'amount': self._parse_amount(line[6 if is_actual else budget_column])
            }

        else:
            return {
                'is_expense': False,
                'is_actual': is_actual,
                'ec_code': self.clean(line[0])[:-2],
                'ic_code': self.clean(line[1])[1:],
                'item_number': self.clean(line[0])[-2:],    # Last two digits
                'description': line[3],
                'amount': self._parse_amount(line[6 if is_actual else 5])
            }

