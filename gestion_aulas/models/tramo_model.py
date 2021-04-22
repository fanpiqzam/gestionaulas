# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class tramo_model(models.Model):
    _name = 'gestion_aulas.tramo_model'
    _description = 'gestion_aulas.tramo_model'

    numero = fields.Integer(string="número")
    reservas = fields.One2many('gestion_aulas.reservas_model', 'tramo_id')
    actividades_id = fields.One2many('gestion_aulas.actividades_model', 'tramo_id')