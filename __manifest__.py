{
    'name': "Empresa",

    'summary': "Gestion de proyectos empresariales",

    'description': """
        Modulo con gestion de proyectos empresariales, permitiendo crear, actualizar y seguir el progreso de los proyectos dentro de una empresa.
    """,

    'author': "IES Juan Bosco",
    'website': "https://www.iesjuanbosco.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/actividad.xml',
        'views/proyecto.xml',
        'views/trabajo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

