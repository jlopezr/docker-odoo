from odoo import fields, api, models

class ApplicationTheme(models.Model):
    _name = "resources.application_theme"
    _description = "Research Application Themes"

    name = fields.Char(required=True, translate=True)