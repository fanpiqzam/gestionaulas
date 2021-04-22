# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class asignaturas_model(models.Model):
    _name = 'gestion_aulas.asignaturas_model'
    _description = 'gestion_aulas.asignaturas_model'

    name = fields.Char(string="Nombre", required=True)
    abreviatura = fields.Char(string="Abreviatura", required=True)
    actividades_id = fields.One2many('gestion_aulas.actividades_model', 'asignatura_id')