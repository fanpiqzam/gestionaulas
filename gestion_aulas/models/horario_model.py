# -*- coding: utf-8 -*-

from odoo import models, fields, api



class horario_model(models.Model):
    _name = 'gestion_aulas.horario_model'
    _description = 'gestion_aulas.horario_model'

    grupo_id = fields.Many2one("gestion_aulas.grupo_model")
    aula_id = fields.Many2one("gestion_aulas.aulas_model")
    tramo_id = fields.Many2one("gestion_aulas.tramo_model")
    asignatura_id = fields.Many2one("gestion_aulas.asignatura_model")