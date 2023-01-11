# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /mnt/extra-addons/library(models.Model):
#     _name = '/mnt/extra-addons/library./mnt/extra-addons/library'
#     _description = '/mnt/extra-addons/library./mnt/extra-addons/library'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
