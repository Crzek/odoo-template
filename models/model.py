from odoo import models, fields


class Todo(models.Model):
    __name__ = "Tareas"

    name = fields.Char("Nombre")
    status = fields.Selection(
        selection=[("borrador", "Borrado"), ("hecho", "Hecho")])
