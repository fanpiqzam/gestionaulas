# -*- coding: utf-8 -*-

from odoo import models, fields, api


class aulas_model(models.Model):
    _name = 'gestion_aulas.aulas_model'
    _description = 'gestion_aulas.aulas_model'
    _order="name"

    name = fields.Char(string="Nombre", required=True)
    abreviatura = fields.Char(string="Abreviatura", required=True)
    reserva_id = fields.One2many("gestion_aulas.reserva_model", "aula_id")
    horario_id = fields.One2many("gestion_aulas.horario_model", "aula_id")