# -*- coding: utf-8 -*-
{
    'name': "everlast_fixes",

    'summary': """
        Customization for Everlast Wellness
        """,

    'description': """
        A module aimed at making some modifications to odoo in order to
        fit business requirements of Everlast Wellness Medical Center L.L.C
    """,

    'author': "Meena Erian",
    'website': "https://www.everlastwellness.com",
    

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
