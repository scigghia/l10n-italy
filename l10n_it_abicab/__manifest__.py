# Copyright 2015 Associazione Odoo Italia (<http://www.odoo-italia.org>)
# Copyright 2016 Davide Corio (Abstract)
# Copyright 2018 Sergio Zanchetta (Associazione PNLUG - Gruppo Odoo)
# Copyright 2020 Matteo Boscolo (https://www.omniasolutions.website)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Italian localization - Codici bancari ABI/CAB',
    'version': '14.0.0.0.1',
    'category': 'Localization/Italy',
    'development_status': 'Production/Stable',
    'summary': 'Base Bank ABI/CAB codes',
    'author': "Odoo Italia Network, Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/l10n-italy/tree/14.0/l10n_it_abicab',
    'license': 'AGPL-3',
    'depends': ['account'],
    'data': ['views/abicab_view.xml'],
    'installable': True,
}
