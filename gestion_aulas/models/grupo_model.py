# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class grupo_model(models.Model):
    _name = 'gestion_aulas.grupo_model'
    _description = 'gestion_aulas.grupo_model'

    name = fields.Char(string="Nombre", required=True)
    abreviatura = fields.Char(string="Abreviatura", required=True)
    actividades = fields.Many2many('gestion_aulas.actividades_model')