# -*- encoding: utf-8 -*-

{
    'name': 'Odoo 15 Account Bank Statement Import',
    'version': '15.0.2.2.0',
    'category': 'Accounting',
    'depends': ['account'],
    'website': 'https://www.odoomates.tech',
    'author': 'Odoo Mates, Odoo SA',
    'support': 'odoomates@gmail.com',
    'maintainer': 'Odoo Mates',
    'license': 'LGPL-3',
    'description': """Generic Wizard to Import Bank Statements In Odoo15 Community Edition.
(This module does include any CSV and XLSX type import format.)""",
    'data': [
        'security/ir.model.access.csv',
        'wizard/journal_creation.xml',
        'views/account_bank_statement_import_view.xml',
        # 'views/res_config_settings_views.xml',
    ],
    'demo': [
        'demo/partner_bank.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': True,
}
