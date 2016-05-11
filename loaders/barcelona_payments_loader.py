# -*- coding: UTF-8 -*-
from budget_app.loaders import PaymentsLoader
from budget_app.models import Budget

class BarcelonaPaymentsLoader(PaymentsLoader):

    # Parse an input line into fields
    def parse_item(self, budget, line):
        # Instead of using the descriptions in the input file (which are in catalan),
        # we use the area/policy and programme ids to fetch the descriptions in
        # the language being loaded.
        area_id = line[0].strip()
        area = Budget.objects.get_all_descriptions(budget.entity)['functional'][area_id]

        programme_id = line[2].strip()
        programme = Budget.objects.get_all_descriptions(budget.entity)['functional'][programme_id]

        # We've been asked to clarify the description of the anonymized payee
        payee = self._titlecase(line[4].strip())
        if payee == 'Anonimitzat':
            payee = {
                'ca': 'Anonimitzat (per compliment normativa protecció de dades personals)',
                'es': 'Anonimizado (por cumplimento normativa protección de datos personales)',
                'en': 'Anonimized (to comply with data protection regulations)'
            }[budget.entity.language]

        return {
            'area': area,
            'programme': programme,
            'fc_code': None,  # We don't try (yet) to have foreign keys to existing records
            'ec_code': None,
            'date': None,
            'contract_type': None,
            'payee': payee,
            'description': self._spanish_titlecase(line[5].strip()),
            'amount': self._read_english_number(line[6])
        }
