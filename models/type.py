from odoo import models, fields, api
class Type(models.Model):
    _name = "type"
    _rec_name = 'lib'
    lib = fields.Text()
    description = fields.Text()