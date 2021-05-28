# -*- coding: utf-8 -*-
# from odoo import http


# class GestionAulas(http.Controller):
#     @http.route('/gestion_aulas/gestion_aulas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_aulas/gestion_aulas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_aulas.listing', {
#             'root': '/gestion_aulas/gestion_aulas',
#             'objects': http.request.env['gestion_aulas.gestion_aulas'].search([]),
#         })

#     @http.route('/gestion_aulas/gestion_aulas/objects/<model("gestion_aulas.gestion_aulas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_aulas.object', {
#             'object': obj
#         })
