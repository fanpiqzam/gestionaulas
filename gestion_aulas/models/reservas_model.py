# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta
import datetime


class reservas_model(models.Model):
    _name = 'gestion_aulas.reservas_model'
    _description = 'gestion_aulas.reservas_model'

    profesor_id = fields.Many2one("gestion_aulas.profesor_model", string="Profesor")
    aula_id = fields.Many2one("gestion_aulas.aulas_model", string="Aula")
    dia = fields.Datetime(string="Día", required=True)
    estado = fields.Selection([("bloqueado","Bloqueado"),("reservado","Reservado")])
    tramo_id = fields.Many2one("gestion_aulas.tramo_model", string="Tramo")
    descripcion = fields.Html(string="Descripción")

    #@api.depends("dia","hora")
    #def _get_fecha(self):
    #    if self.dia and self.hora:
    #        tmp = str (self.dia).split(" ")[0] + ' ' + str(self.hora)+":00"
    #        self.dia = tmp
    #        self.fecha_fin = self.dia + datetime.timedelta(minutes=55)
