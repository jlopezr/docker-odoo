# -*- coding: utf-8 -*-
# from odoo import http


# class ResourcesApp(http.Controller):
#     @http.route('/resources_app/resources_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/resources_app/resources_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('resources_app.listing', {
#             'root': '/resources_app/resources_app',
#             'objects': http.request.env['resources_app.resources_app'].search([]),
#         })

#     @http.route('/resources_app/resources_app/objects/<model("resources_app.resources_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('resources_app.object', {
#             'object': obj
#         })
