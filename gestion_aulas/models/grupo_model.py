# -*- coding: utf-8 -*-

from odoo import models, fields, api



class grupo_model(models.Model):
    _name = 'gestion_aulas.grupo_model'
    _description = 'gestion_aulas.grupo_model'

    name = fields.Char(string="Nombre", required=True)
    abreviatura = fields.Char(string="Abreviatura", required=True)
    horario_id = fields.One2many("gestion_aulas.horario_model", "grupo_id")