# -*- coding: utf-8 -*-
from odoo import models, fields
from . import borrar_datos
from odoo.exceptions import ValidationError

class borrar_wizard(models.TransientModel):
    _name = "gestion_aulas.borrar_wizard"
    _description = "gestion_aulas.borrar_wizard"

    usuario = fields.Char(string="Usuario", required=True)
    contrasenya = fields.Char(string="Contraseña", required=True)
    host = fields.Char(string="Host", required=True)
    database = fields.Char(string="Base de datos", required=True)

    def borrar_datos(self):
        borrar_datos.borrar_reservas(self.host, self.database, self.usuario, self.contrasenya)
        borrar_datos.borrar_horario(self.host, self.database, self.usuario, self.contrasenya)
        borrar_datos.borrar_tramos(self.host, self.database, self.usuario, self.contrasenya)
        borrar_datos.borrar_profesores(self.host, self.database, self.usuario, self.contrasenya)
        borrar_datos.borrar_aulas(self.host, self.database, self.usuario, self.contrasenya)
        borrar_datos.borrar_grupos(self.host, self.database, self.usuario, self.contrasenya)
        borrar_datos.borrar_asignatura(self.host, self.database, self.usuario, self.contrasenya)
        borrar_datos.alter_secuencias(self.host, self.database, self.usuario, self.contrasenya)