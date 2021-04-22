# -*- coding: utf-8 -*-

from odoo import models, fields, api



class aulas_model(models.Model):
    _name = 'gestion_aulas.aulas_model'
    _description = 'gestion_aulas.aulas_model'
    _order="name"

    name = fields.Char(string="Nombre", required=True)
    abreviatura = fields.Char(string="Abreviatura", required=True)
    actividades_id = fields.One2many('gestion_aulas.actividades_model', 'aula_id')