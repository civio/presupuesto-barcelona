# -*- coding: UTF-8 -*-
from budget_app.loaders import PaymentsLoader

class BarcelonaPaymentsLoader(PaymentsLoader):

    # Parse an input line into fields
    def parse_item(self, budget, line):
        return {
            'area': line[3].strip(),
            'fc_code': '',
            'ec_code': '',
            'date': None,
            'contract_type': '',
            'payee': self._titlecase(line[4].strip()),
            'description': self._spanish_titlecase(line[5].strip()),
            'amount': self._read_english_number(line[6])
        }
