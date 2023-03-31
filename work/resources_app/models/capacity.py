from odoo import fields, models, api

class resourcesCapacity(models.Model):
    _name = "resources.capacity"
    _description = "Capacities"
    name = fields.Char("Name", required=True)
    description = fields.Html(string="Description")
    home_partner_institution = fields.Many2one("res.partner", string="Home partner institution")
    keywords = fields.Many2many('resources.keyword', string="Keywords")
    image = fields.Binary(string="Image")
