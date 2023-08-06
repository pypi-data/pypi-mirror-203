# -*- coding: utf-8 -*-
{
    'name': "crm_cooperator_rest_api",

    'summary': """
        Expose CRM Cooperator on the Rest API""",

    'author': "Coopdevs Treball SCCL",
    'website': "",

    'category': 'api',
    'version': '12.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'crm_cooperator',
        'crm_rest_api'
    ],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
}
