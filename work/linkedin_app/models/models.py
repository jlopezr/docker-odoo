# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class linkedin_app(models.Model):
#     _name = 'linkedin_app.linkedin_app'
#     _description = 'linkedin_app.linkedin_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
