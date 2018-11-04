# -*- coding: utf-8 -*-
#
#    Copyright (C) 2017 Apulia Software s.r.l. (http://www.apuliasoftware.it)
#    @author Francesco Apruzzese <f.apruzzese@apuliasoftware.it>
#   Andrea Cometa <a.cometa@apuliasoftware.it>
#
#    License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Italian Localisation - Natura delle aliquote IVA',
    'version': '0.0.1',
    'category': 'Localisation/Italy',
    'author': "Odoo Community Association (OCA), Apulia Software s.r.l",
    'website': 'https://www.odoo-italia.net/',
    'license': 'AGPL-3',
    'depends': [
        'account',
        ],
    'data': [
        'view/account_tax_kind_view.xml',
        'view/account_tax_view.xml',
        'data/account.tax.kind.csv',
        'security/ir.model.access.csv',
        ],
    'installable': True
}
