
# -*- coding: utf-8 -*-
{
    'name': "Odoo printers module",

    'summary': """installation module""",

    'description': """
        dependencies installation and custom module for remote printers data handling
    """,

    'author': "ImPossibleTech",
    'website': "http://www.impossibletech.it",


    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    #'depends': ['base','sale','stock','purchase'],

    # always loaded
    'data': [
	#'data/data.xml',
        'views/odoo_printers_views.xml',
        #'views/inherit_view.xml',
        #'views/web_template.xml',
        #'security/viper_base_security.xml',
        #'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}




