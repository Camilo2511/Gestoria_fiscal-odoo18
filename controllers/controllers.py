# -*- coding: utf-8 -*-
# from odoo import http


# class GestoriaFiscal(http.Controller):
#     @http.route('/gestoria_fiscal/gestoria_fiscal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestoria_fiscal/gestoria_fiscal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestoria_fiscal.listing', {
#             'root': '/gestoria_fiscal/gestoria_fiscal',
#             'objects': http.request.env['gestoria_fiscal.gestoria_fiscal'].search([]),
#         })

#     @http.route('/gestoria_fiscal/gestoria_fiscal/objects/<model("gestoria_fiscal.gestoria_fiscal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestoria_fiscal.object', {
#             'object': obj
#         })

