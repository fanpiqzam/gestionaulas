# -*- coding: utf-8 -*-

from odoo import models, fields, api



class profresor_model(models.Model):
    _name = "gestion_aulas.profesor_model"
    _description = "gestion_aulas.profesor_model"

    name = fields.Char(string="Nombre")
    abreviatura = fields.Char(string="Abreviatura")
    reserva = fields.One2many("gestion_aulas.reserva_model", "profesor_id")