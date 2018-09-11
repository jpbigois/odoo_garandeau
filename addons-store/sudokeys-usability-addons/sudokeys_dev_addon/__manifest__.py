# -*- coding: utf-8 -*-
{
	'name': "Sudokeys Developer Addon",
	'description': """ """,
	'category': "Tools",
	'installable': True,
	'application': False,
	'author' : 'Sudokeys',
	'website': 'http://www.sudokeys.com',
	'depends' : [
		'base',
		'sudokeys_appswitcher_improved',
		'update_module_list',
	],
	'data': [
		'data/sdk_dev_script_data.xml',
		'views/ir_model_data_views.xml',
	],
}
