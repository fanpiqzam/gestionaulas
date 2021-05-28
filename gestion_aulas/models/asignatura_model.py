# -*- coding: utf-8 -*-

from odoo import models, fields, api



class asignatura_model(models.Model):
    _name = 'gestion_aulas.asignatura_model'
    _description = 'gestion_aulas.asignatura_model'
    _order="name"

    name = fields.Char(string="Nombre")
    abreviatura = fields.Char(string="Abreviatura")
    horario_id = fields.One2many("gestion_aulas.horario_model", "asignatura_id")