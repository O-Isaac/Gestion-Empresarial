from odoo import models, fields, api
from math import floor

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

    # Autocalculado
    progreso_total = fields.Integer(string="Total de progreso", compute="_compute_total")

    # Funcion autocalculado
    @api.depends("actividades_ids", "actividades_ids.estado")
    def _compute_total(self):
        for trabajo in self:
            actividades_totales = len(trabajo.actividades_ids)

            if actividades_totales > 0:
                actividades_finalizadas = len(trabajo.actividades_ids.filtered(lambda x: x.estado == 'finalizado'))
                trabajo.progreso_total = floor((actividades_finalizadas / actividades_totales) * 100)
            else:
                trabajo.progreso_total = 0

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
    actividades_ids = fields.One2many("empresa.actividad", "trabajo_id", string="Actividades")