from odoo import models, fields


class Todo(models.Model):
    _name = "ot.todo"

    name = fields.Char("Nombre")
    status = fields.Selection(
        selection=[("borrador", "Borrado"), ("hecho", "Hecho")])
