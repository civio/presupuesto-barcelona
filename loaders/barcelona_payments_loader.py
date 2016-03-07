# -*- coding: UTF-8 -*-
from budget_app.loaders import PaymentsLoader

class BarcelonaPaymentsLoader(PaymentsLoader):

    # Parse an input line into fields
    def parse_item(self, budget, line):
        return {
            'area': line[1].strip(),
            'programme': line[3].strip(),
            'fc_code': None,  # We don't try (yet) to have foreign keys to existing records
            'ec_code': None,
            'date': None,
            'contract_type': None,
            'payee': self._titlecase(line[4].strip()),
            'description': self._spanish_titlecase(line[5].strip()),
            'amount': self._read_english_number(line[6])
        }
