# -*- coding: utf-8 -*-
# from odoo import http


# class Caq3(http.Controller):
#     @http.route('/caq3/caq3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/caq3/caq3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('caq3.listing', {
#             'root': '/caq3/caq3',
#             'objects': http.request.env['caq3.caq3'].search([]),
#         })

#     @http.route('/caq3/caq3/objects/<model("caq3.caq3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('caq3.object', {
#             'object': obj
#         })
