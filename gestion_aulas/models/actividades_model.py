# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class actividades_model(models.Model):
    _name = 'gestion_aulas.actividades_model'
    _description = 'gestion_aulas.actividades_model'

    aula_id = fields.Many2one('gestion_aulas.aulas_model')
    tramo_id = fields.Many2one('gestion_aulas.tramo_model')
    asignatura_id = fields.Many2one('gestion_aulas.asignaturas_model')
    profesor_id = fields.Many2one('gestion_aulas.profesor_model')
    grupo = fields.Many2many('gestion_aulas.grupo_model')