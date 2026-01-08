from odoo import models, fields, api
from math import floor

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

    # Autocalculados
    progreso_total = fields.Integer(string="Progreso", compute='_compute_progreso')

    # Funcion del autocalculado
    @api.depends("trabajos_ids", "trabajos_ids.estado")
    def _compute_progreso(self):
        for proyecto in self:
            total_trabajos = len(proyecto.trabajos_ids)

            if total_trabajos > 0:
                # Contar trabajos finalizados
                trabajos_finalizados = len(proyecto.trabajos_ids.filtered(lambda t: t.estado == 'finalizado'))

                # Se calcula
                proyecto.progreso_total = floor((trabajos_finalizados / total_trabajos) * 100)
            else:
                proyecto.progreso_total = 0


    # Campos
    nombre = fields.Char(string="Nombre del Proyecto", required=True)
    descripcion = fields.Text(string="Descripción del Proyecto", required=True)
    fecha_inicio = fields.Date(string="Fecha de Inicio", required=True, default=fields.Date.today())
    fecha_fin = fields.Date(string="Fecha de Fin", ºrequired=True)
    estado = fields.Selection(_estados_proyecto, string='Estado del Proyecto', default='borrador', required=True)

    # Relaciones
    responsable = fields.Many2one('res.users', string="Responsable del Proyecto", required=True)
    trabajos_ids = fields.One2many('empresa.trabajo', 'proyecto_id', string="Trabajos Asociados")
