from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ResUsers(models.Model):
    _inherit = 'res.users'

    linkedin = fields.Char()

    @api.constrains('linkedin', 'linkedin_confirm')
    def _check_linkedin(self):
        for record in self:
            if record.linkedin:
                partner = record.partner_id
                if partner:
                    partner.write({
                        'linkedin': record.linkedin,
                        'linkedin_confirm': True
                    })
                    partner._check_linkedin()