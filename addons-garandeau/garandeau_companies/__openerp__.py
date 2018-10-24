# -*- coding: utf-8 -*-
{
    'name': "Garandeau_companies",

    'summary': """
        Module initiale garandeau Garandeau""",

    'description': """
        Ce module cree les societes du groupe garandeau et le modifie la structure d une societe 
        pour y ajouter un code societe (code interne) ...
        ATTENTION : Cette version est module est modifiee pour l u
    """,

    'author': "Groupe Garandeau",
    'website': "http://www.garandeau.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Garandeau',
    'version': '10.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web', 'hr', 'fleet', 'sale', 'calendar' , 'hr', 'l10n_fr_siret'],

    # always loaded
    'data': [
        'data/societe_garandeau.xml',

        # 'security/ir.model.access.csv',
        'views/views.xml',              #Menu root principal
        'views/company.xml',
        'views/taxes.xml',


    ],
    # Test js :
    # 'chauffeurs': ['static/src/js/chauffeurs.js'],
    # 'js': ['static/src/js/chauffeurs.js'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install' : False,
}