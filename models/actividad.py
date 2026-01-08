from odoo import models, fields

class Actividad(models.Model):
    _name = 'empresa.actividad'
    _description = 'Modelo para gestionar proyectos empresariales'
    _rec_name = 'nombre'

    _estados = [
        ('pendiente', 'Pendiente'),
        ('en_curso', 'En Curso'),
        ('en_revision', 'En Revision'),
        ('en_planificacion', 'En Planificacion'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado')
    ]

    nombre = fields.Char(string="Nombre de la actividad")
    detalle = fields.Text(string="Detalle de la actividad")
    persona = fields.Many2one('res.users', string="Responsable del Trabajo", required=True)
    inicio_planificado = fields.Date(string="Fecha de inicio", required=True, default=fields.Date.today())
    final_planificado = fields.Date(string="Fecha de final", required=True, default=fields.Date.today())
    estado = fields.Selection(_estados, string='Estado de la actividad', default='pendiente', required=True)
    trabajo_id = fields.Many2one('empresa.trabajo', string="Trabajo")
