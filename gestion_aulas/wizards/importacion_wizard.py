# -*- coding: utf-8 -*-
from odoo import api, models, fields
from . import importacion_datos
from odoo.exceptions import ValidationError
import base64
from io import BytesIO

class importacion_wizard(models.TransientModel):
    _name = "gestion_aulas.importacion_wizard"
    _description = "gestion_aulas.importacion_wizard"

    name = fields.Char(string="Nombre")
    archivo = fields.Binary(string="Archivo")
    usuario = fields.Char(string="Usuario", required=True)
    contrasenya = fields.Char(string="Contraseña", required=True)
    host = fields.Char(string="Host", required=True)
    database = fields.Char(string="Base de datos", required=True)
    fin_curso = fields.Datetime(string="Final de curso", required=True)


    @api.constrains('archivo')
    def _check_archivo(self):
        if self.archivo == False:
            raise ValidationError("No ha introducido ningún archivo")

    def importar_datos(self):
        file_to_decode = base64.b64decode(self.archivo)
        importacion_datos.insertar_asignaturas(BytesIO(file_to_decode), self.host, self.database, self.usuario, self.contrasenya)
        importacion_datos.insert_grupos(BytesIO(file_to_decode), self.host, self.database, self.usuario, self.contrasenya)
        importacion_datos.insert_aulas(BytesIO(file_to_decode), self.host, self.database, self.usuario, self.contrasenya)
        importacion_datos.insert_profesores(BytesIO(file_to_decode), self.host, self.database, self.usuario, self.contrasenya)
        importacion_datos.insert_tramos(BytesIO(file_to_decode), self.host, self.database, self.usuario, self.contrasenya)
        importacion_datos.insert_horario(BytesIO(file_to_decode), self.host, self.database, self.usuario, self.contrasenya)
        importacion_datos.insert_horario_reservas(BytesIO(file_to_decode), self.host, self.database, self.usuario, self.contrasenya,self.fin_curso)