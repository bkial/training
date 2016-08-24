# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'views/course.xml',
        'demo.xml',
        'views/session.xml',
        'views/partner.xml',
        'workflow/session_workflow.xml',
        'wizard/wizard.xml',
        'report/session_report_qweb.xml',
        'report/session_report_webkit.xml',
        'dashboard/session_dashboard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}