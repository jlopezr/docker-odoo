# -*- coding: utf-8 -*-
# from odoo import http


# class LinkedinApp(http.Controller):
#     @http.route('/linkedin_app/linkedin_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/linkedin_app/linkedin_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('linkedin_app.listing', {
#             'root': '/linkedin_app/linkedin_app',
#             'objects': http.request.env['linkedin_app.linkedin_app'].search([]),
#         })

#     @http.route('/linkedin_app/linkedin_app/objects/<model("linkedin_app.linkedin_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('linkedin_app.object', {
#             'object': obj
#         })
