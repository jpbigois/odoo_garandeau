# -*- coding: utf-8 -*-
{
    'name': "Garandeau_tools",

    'summary': """
        Tools garandeau Garandeau""",

    'description': """
        
    """,

    'author': "Groupe Garandeau",
    'website': "http://www.garandeau.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Garandeau',
    'version': '10.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'l10n_fr_siret'],

    # always loaded
    'data': [


    ],
    # Test js :
    # 'chauffeurs': ['static/src/js/chauffeurs.js'],
    # 'js': ['static/src/js/chauffeurs.js'],
    # only loaded in demonstration mode
    'demo': [
        # demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install' : False,
}
