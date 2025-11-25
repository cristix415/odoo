# -*- coding: utf-8 -*-
{
    'name': "caq3",
    'summary': "Demo module CAQ3",
    'description': "Module demo cu homepage și model simplu",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'web'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'caq3/static/src/js/caq3_home.js',
        ],
    },
    'installable': True,
    'application': True,
    'demo': [
        'demo/demo.xml',
    ],
}
