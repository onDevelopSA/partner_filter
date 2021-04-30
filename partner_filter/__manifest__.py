# -*- coding: utf-8 -*-
# © 2021 onDevelop.sa
# Autor: Idelis Gé Ramírez
# Part of onDevelop.SA. See LICENSE file for full copyright and licensing details.
{
    'name': "partner_filter",
    'summary': """Filter partners between customer or supplier.""",
    'description': """
        Only the customers are selectables in the Quotation view and  only the
        suppliers in the purchase view.
    """,
    'author': "onDevelop.SA",
    'website': "https://ondevelop.tech/",
    'category': 'Sales/Purchase/Human Resources',
    'version': '14.0.1',
    'license': 'OPL-1',
    'price': 9,
    'currency': 'USD',
    'support': "ondevelop.sa@gmail.com",
    'depends': ['base', 'sale', 'purchase'],
    'images': ['static/description/partner_filter_cover.png'],
    'data': ['views/sale_order.xml',
             'views/purchase_view.xml'],
    'demo': ['demo/demo.xml'],
    'installable': True,
    'auto_install': False
}
