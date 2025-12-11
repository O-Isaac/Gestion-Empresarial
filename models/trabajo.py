from odoo import models, fields


class Trabajo(models.Model):
    _name = 'empresa.trabajo'
    _description = 'Modelo para gestionar trabajos empresariales'
    _rec_name = 'nombre'
    _estados = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('en_revision', 'En Revisión'),
        ('finalizado', 'Finalizado'),
    ]
    _prioridad = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]

    # Campos
    nombre = fields.Char(string="Nombre del Trabajo", required=True)
    descripcion = fields.Text(string="Descripción del Trabajo", required=True)
    fecha_inicio = fields.Date(string="Fecha de Inicio", required=True, default=fields.Date.today())
    fecha_fin = fields.Date(string="Fecha de Fin", required=True)
    estado = fields.Selection(_estados, string='Estado del Trabajo', default='pendiente', required=True)
    prioridad = fields.Selection(_prioridad, string='Prioridad del Trabajo', default='media', required=True)

    # Relaciones
    responsable = fields.Many2one('res.users', string="Responsable del trabajo", required=True)
    proyecto_id = fields.Many2one('empresa.proyecto', string="Proyecto Asociado", required=True)