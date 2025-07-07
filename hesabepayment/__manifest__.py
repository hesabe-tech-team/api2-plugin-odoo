# -*- coding: utf-8 -*-
{
    'name': 'Payment Provider: Hesabe',
    'summary': 'Hesabe – Payment Gateway',
    'maintainer': 'Hesabe Tech Team',
    'category': 'Accounting/Payment Providers',
    'author': "Hesabe Company for Electronic Payments & Settlements ",
    'depends': ['payment'],
    'website': "https://developer.hesabe.com/docs/Odoo-Latest",
    'version': '0.0.1',
    'price': 49.99,
    'currency': 'USD',
    'sequence': -97,
    'description': """Hesabe Payment Gateway for Odoo 18.0""",
    'company': 'Hesabe Company for Electronic Payments & Settlements',
    'data': [
        # 'security/ir.model.access.csv',
        'views/payment_hesabe_template.xml',
        'views/payment_views.xml',
        'data/payment_method_data.xml',
        'data/payment_provider_data.xml',
    ],
    'images': ['static/description/Banner.PNG'],
    'assets': {
        'web.assets_backend': [
            'hesabepayment/static/src/style.css'
        ],
    },
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
}
