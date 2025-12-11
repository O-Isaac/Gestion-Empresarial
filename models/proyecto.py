from odoo import models, fields

class Proyecto(models.Model):
    _name = 'empresa.proyecto'
    _description = 'Modelo para gestionar proyectos empresariales'
    _estados_proyecto = [
        ('borrador', 'Borrador'),
        ('en_progreso', 'En Progreso'),
        ('en_ejecucion', 'En Ejecución'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado')
    ]
    _rec_name = 'nombre'

    # Campos
    nombre = fields.Char(string="Nombre del Proyecto", required=True)
    descripcion = fields.Text(string="Descripción del Proyecto", required=True)
    fecha_inicio = fields.Date(string="Fecha de Inicio", required=True, default=fields.Date.today())
    fecha_fin = fields.Date(string="Fecha de Fin", required=True)
    estado = fields.Selection(_estados_proyecto, string='Estado del Proyecto', default='borrador', required=True)

    # Relaciones
    responsable = fields.Many2one('res.users', string="Responsable del Proyecto", required=True)
    trabajos_ids = fields.One2many('empresa.trabajo', 'proyecto_id', string="Trabajos Asociados")