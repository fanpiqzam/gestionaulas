# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, timedelta
from datetime import datetime
import logging
import calendar
import pytz
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
    
    periodica = fields.Boolean(string="Reserva periódica", default=False)
    fecha_fin_peri = fields.Datetime(string="Hasta fecha")

    @api.depends("dia","hora")
    def _get_fecha(self):    
        if self.dia and self.hora:
            #user_tz = self.env.user.tz or pytz.utc
            #local = pytz.timezone(user_tz)
            tmp = str(self.dia).split(" ")[0] + ' ' + str(self.hora)+":00" 
            self.dia = tmp
            #self.dia = datetime.strftime(pytz.utc.localize(datetime.strptime(tmp, "%Y-%m-%d %H:%M:%S")).astimezone(local))
            self.fecha_fin = self.dia + timedelta(minutes=55)

    """@api.onchange('fecha_fin_peri')
    def create(self):
        for record in self:
            if record.periodica == True:
                dia_sig = record.dia
                _logger.info(dia_sig)
                while dia_sig <= record.fecha_fin_peri:
                    record = record.env['gestion_aula.reserva_model'].create({
                            'name' : record.name,
                            'aula_id' : record.aula_id,
                            'dia' : dia_sig,
                            'hora' : record.hora,
                            'profesor_id' : record.profesor_id,
                            'fecha_fin' : record.fecha_fin,
                            'periodica' : True,
                            'fecha_fin_peri' : record.fecha_fin_peri
                    })
                    _logger.info(dia_sig)
                    _logger.info(self.aula_id)
                    dia_sig = self.dia + timedelta(days=7)
                    _logger.info(dia_sig)
                    return record
            else:
                return None"""
    
    @api.constrains('dia')
    def _checkDate(self):
        hoy = datetime.today()
        if (self.dia < hoy):
            raise ValidationError("La fecha y hora no pueden ser anteriores a la fecha y hora actuales.")

    #def _get_tramo(self):
    #    day_of_week = calendar.day_name[self.dia.weekday()]
    #    _logger.info(day_of_week)
    #    _logger.info(self.hour)
    #    obj = self.env['gestion_aulas.tramo_model']
    #    obj.search([('dia','=',day_of_week), ('hora','=',hora)], limit=1)
