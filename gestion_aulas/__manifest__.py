# -*- coding: utf-8 -*-
{
    'name': "GestionAulas",

    'summary': """
        Módulo para la gestión y reserva de aulas de un centro educativo.""",

    'description': """
        Módulo para la gestión y reserva de aulas de un centro educativo.
    """,

    'author': "Fanny Piqueres",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/tramo_view.xml',
        'views/reservas_view.xml',
        'views/aula_view.xml',
        'views/horario_view.xml',
        'views/grupo_view.xml',
        'views/asignaturas_view.xml',
        'wizards/borrar_datos_wizard.xml',
        'wizards/importacion_wizard.xml',
        'views/profesor_view.xml',
        'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
