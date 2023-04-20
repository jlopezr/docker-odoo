import logging
from odoo import fields, models, api

_logger = logging.getLogger(__name__)

class resourcesInfrastructure(models.Model):
    _name = "resources.infrastructure"
    _description = "Infrastructures"
    name = fields.Char("Name", required=True)
    description = fields.Html(string="Description")
    home_partner_institution = fields.Many2one("res.partner", string="Home partner institution")
    contact_person = fields.Many2many("res.partner", string="Contact persons")
    equipment = fields.Char("Equipment")
    keywords = fields.Many2many('resources.keyword', string="Keywords")
    technical_staff = fields.Boolean(string="Own technical staff")
    booking_system = fields.Boolean(string="Existing booking system to host external user")
    remote_access_policy = fields.Boolean(string="Established remote access policy")
    research_application_theme = fields.Many2many('resources.application_theme', string="Research Application Themes", no_create=True)
    image = fields.Binary(string="Image")
    web_link = fields.Char(string="Website", widget="url")

