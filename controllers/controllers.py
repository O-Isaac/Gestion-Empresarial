# from odoo import http


# class Gestion-empresarial(http.Controller):
#     @http.route('/gestion-empresarial/gestion-empresarial', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion-empresarial/gestion-empresarial/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion-empresarial.listing', {
#             'root': '/gestion-empresarial/gestion-empresarial',
#             'objects': http.request.env['gestion-empresarial.gestion-empresarial'].search([]),
#         })

#     @http.route('/gestion-empresarial/gestion-empresarial/objects/<model("gestion-empresarial.gestion-empresarial"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion-empresarial.object', {
#             'object': obj
#         })

