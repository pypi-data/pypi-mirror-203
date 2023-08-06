# -*- coding: utf-8 -*-
{
    'name': "crm_cooperator",

    'summary': """
        Add relationship between crm and subscription_request""",

    'author': "Coopdevs Treball SCCL",
    'website': "",

    'category': 'cooperator',
    'version': '12.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'easy_my_coop'],

    # always loaded
    'data': [
        'views/crm_lead.xml',
    ],
    # only loaded in demonstration mode
}
