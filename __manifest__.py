# -*- coding: utf-8 -*-
{
    'name': "Exercice",

    'summary': """
        exercice de test""",

    'description': """
        Ce module ajoute des modifications  pour le process de vente
    """,

    'author': "bernous abd sallem",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'report/sale_order_rapport.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
      #  'demo/demo.xml',
    ],
}