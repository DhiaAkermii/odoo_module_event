from odoo import models, fields, api
class Participants(models.Model):
    _name = 'participant'
    _rec_name = 'prenom'
    nom = fields.Text()
    prenom = fields.Text()
    cin = fields.Integer()
    phone = fields.Integer()
    mail = fields.Text()
    event_id = fields.Many2many(comodel_name='university.student',string="Evenements")