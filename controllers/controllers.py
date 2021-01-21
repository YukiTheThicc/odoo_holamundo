# -*- coding: utf-8 -*-
# from odoo import http


# class OdooHolamundo(http.Controller):
#     @http.route('/odoo_holamundo/odoo_holamundo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_holamundo/odoo_holamundo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_holamundo.listing', {
#             'root': '/odoo_holamundo/odoo_holamundo',
#             'objects': http.request.env['odoo_holamundo.odoo_holamundo'].search([]),
#         })

#     @http.route('/odoo_holamundo/odoo_holamundo/objects/<model("odoo_holamundo.odoo_holamundo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_holamundo.object', {
#             'object': obj
#         })
