# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/library(http.Controller):
#     @http.route('//mnt/extra-addons/library//mnt/extra-addons/library', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/library//mnt/extra-addons/library/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/library.listing', {
#             'root': '//mnt/extra-addons/library//mnt/extra-addons/library',
#             'objects': http.request.env['/mnt/extra-addons/library./mnt/extra-addons/library'].search([]),
#         })

#     @http.route('//mnt/extra-addons/library//mnt/extra-addons/library/objects/<model("/mnt/extra-addons/library./mnt/extra-addons/library"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/library.object', {
#             'object': obj
#         })
