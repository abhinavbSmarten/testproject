# -*- coding: utf-8 -*-
{
    'name': 'cpnepal',
    'version': '1.0.0',
    'category': 'realestate',
    'sequence': 1,
    'summary': 'cp nepal operations',
    'description': """Module to manage cp nepal operations.""",
    'author': 'Smarten Technologies',
    'website': '',
    'depends': ['base','website','crm','invoice','ecommerce','email_marketing','employees'],
    'data': [
        "security/ir.model.access.csv",
        "views/unitcon.xml",
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
    'license': 'AGPL-3'
}
