# -*- coding: utf-8 -*-
{
    'name': "Garandeau_importFactu",

    'summary': """
        Applications d'importation des factu en prévision de Chorus""",

    'description': """
        Dans le cadre de la migration de HS6 nous tentons de basculer
        sur un ERP odoo ...
        Les applications développées dans ce module sont spécifiques au Groupe Garandeau
    """,

    'author': "Groupe Garandeau",
    'website': "http://www.garandeau.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Garandeau',
    'version': '9.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        
    ],
    
    # only loaded in demonstration mode
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'auto_install' : False,
}
