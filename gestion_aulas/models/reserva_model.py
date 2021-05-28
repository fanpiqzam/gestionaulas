# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, timedelta
from datetime import datetime
import logging
import calendar
from odoo.exceptions import ValidationError
from odoo.tools.date_utils import date_range
_logger = logging.getLogger(__name__)


class reserva_model(models.Model):
    _name = 'gestion_aulas.reserva_model'
    _description = 'gestion_aulas.reserva_model'
    _order="name"
    _sql_constraints = [
        ('reserva_unique','UNIQUE(aula_id,dia)','No se puede realizar la reserva'),
    ]


    name = fields.Char(string = "Motivo")
    aula_id = fields.Many2one("gestion_aulas.aulas_model")
    dia = fields.Datetime(string="Día", required=True)
    hora = fields.Selection([("06:00","08:00"),("06:55","08:55"),("07:50","09:50"),("9:15","11:15"),("10:10","12:10"),("11:05","13:05"),("12:00","14:00")], required=True)
    profesor_id = fields.Many2one("res.users",default=lambda self:self.env.user and self.env.user.id or False, string="Profesor")
    fecha_fin = fields.Datetime(string="Fin", compute='_get_fecha',store=True,readonly=True)
    
    periodica = fields.Boolean(string="Reserva periódica")
    fecha_fin_peri = fields.Datetime(string="Hasta fecha")

    @api.depends("dia","hora")
    def _get_fecha(self):
        if self.dia and self.hora:
            tmp = str(self.dia).split(" ")[0] + ' ' + str(self.hora)+":00" 
            self.dia = tmp
            self.fecha_fin = self.dia + timedelta(minutes=55)

    @api.onchange("periodica")
    def _reserva_periodica(self):
        if self.periodica == True:
            dia_sig = self.dia
            _logger.info(dia_sig)
            for d in date_range(self.dia, self.fecha_fin_peri):
                self.env['gestion_aula.reserva_model'].create({
                        'name' : d.name,
                        'aula_id' : d.aula_id,
                        'dia' : dia_sig,
                        'hora' : d.hora,
                        'profesor_id' : d.profesor_id,
                        'fecha_fin' : d.fecha_fin,
                        'periodica' : True,
                        'fecha_fin_peri' : d.fecha_fin_peri
                })
                _logger.info(d.dia_sig)
                _logger.info(d.aula_id)
                dia_sig = self.dia + timedelta(days=7)
                _logger.info(dia_sig)
        else:
            return None
    
    @api.constrains('dia')
    def _checkDate(self):
        hoy = datetime.today()
        if (self.dia < hoy):
            raise ValidationError("La fecha y hora no pueden ser anteriores a la fecha y hora actual.")

    #def _get_tramo(self):
    #    day_of_week = calendar.day_name[self.dia.weekday()]
    #    _logger.info(day_of_week)
    #    _logger.info(self.hour)
    #    obj = self.env['gestion_aulas.tramo_model']
    #    obj.search([('dia','=',day_of_week), ('hora','=',hora)], limit=1)
