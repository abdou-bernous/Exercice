# -*- coding: utf-8 -*-
from odoo import http

# class Exercice(http.Controller):
#     @http.route('/exercice/exercice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exercice/exercice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exercice.listing', {
#             'root': '/exercice/exercice',
#             'objects': http.request.env['exercice.exercice'].search([]),
#         })

#     @http.route('/exercice/exercice/objects/<model("exercice.exercice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exercice.object', {
#             'object': obj
#         })