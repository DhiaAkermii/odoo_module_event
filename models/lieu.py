from odoo import models, fields, api
class Lieu(models.Model):
    _name = 'lieu'
    _rec_name = 'lib'
    lib = fields.Text()
    adresse = fields.Text()