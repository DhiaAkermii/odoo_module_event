# -*- coding: utf-8 -*-
from . import event,lieu,participant,type
from odoo import models, fields, api
class UniversityStudent(models.Model):
    _name = 'university.student'
    _description = 'university.university'
    _rec_name = 'titre'
    titre = fields.Text()
    date = fields.Date()
    duree = fields.Text()
    nombreParticipants = fields.Integer(string='Nombre de participants')
    fraisInscrit = fields.Integer(string = "Frais d'inscription en DT")
    certificate =fields.Selection([('Yes', 'Yes'), ('No', 'No')], 'Certificate')
    type_id = fields.Many2one(comodel_name ='type',string='Type')
    lieu_id = fields.Many2one(comodel_name='lieu')
    participants_ids = fields.Many2many(comodel_name='participant',inverse_name='event_id')
