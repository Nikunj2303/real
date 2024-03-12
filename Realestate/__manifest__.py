# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'author': 'Reliution',
    'version': '15.0.0.2',
    'license': 'LGPL-3',
    'sequence': 1,
    'depends': ['base','account','mail'],
    'data': ['security/ir.model.access.csv',
             'security/security.xml',
             'wizard/appointment_view.xml',
             'views/property_view.xml',
             'views/estate_property.xml',
             'views/property_tag.xml',
             'views/property_type.xml'],
    'auto_install': False,
    'application': True,
    'installable': True,
}
