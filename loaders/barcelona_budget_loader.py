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
        # The budget data we have for 2018 doesn't (yet) have amended expense figures,
        # so in that case we use the initial budget
        year = re.search('municipio/(\d+)/', filename).group(1)
        budget_column = 4 if year in ['2018'] else 5

        is_expense = (filename.find('gastos.csv')!=-1)
        is_actual = (filename.find('/ejecucion_')!=-1)
        if is_expense:
            fc_code = self.clean(line[2]).rjust(5, '0') # Some programmes miss starting 0

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
                'amount': self._parse_amount(line[6 if is_actual else budget_column])
            }

