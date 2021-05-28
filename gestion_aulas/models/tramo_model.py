# -*- coding: utf-8 -*-

from odoo import models, fields, api



class tramo_model(models.Model):
    _name = 'gestion_aulas.tramo_model'
    _description = 'gestion_aulas.tramo_model'

    numero = fields.Char(string="Número tramo")
    dia = fields.Char(string="Día")
    hora = fields.Char(string='Hora')
    horario_id = fields.One2many("gestion_aulas.horario_model", "tramo_id")