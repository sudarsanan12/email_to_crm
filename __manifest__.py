{
    'name': 'Email CRM Lead generation',
    'version': '17.0.0.0.1',
    'category': 'Connector',
    'author': 'Sudarsanan P.R',
    'website': '',
    'summary': 'Connect Email and create leads when a new Booking has come',
    'description': """Email CRM integration""",
    'depends': ['base', 'contacts', 'crm', 'mail', 'account','sale_crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/fetch_mail.xml',
        'views/crm_lead_inherit.xml',
        'wizard/create_invoice_wizard.xml',
        'views/menu.xml',
    ],

    'license': 'OPL-1',
    'application': False,
    'auto_install': False,
    'installable': True,
}
