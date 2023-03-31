from odoo import http

class Resources(http.Controller):
    @http.route("/resources/infrastructure", website=True, auth='my_api_key')
    def list(self, *args, **kwargs):
        Resource = http.request.env["resources.infrastructure"]
        ApplicationTheme = http.request.env["resources.application_theme"]
        Keyword = http.request.env["resources.keyword"]
        resources = Resource.search([])
        universities = http.request.env['res.partner'].search([
            ('id', 'in', resources.mapped('home_partner_institution.id'))
        ])
        applicationThemes = ApplicationTheme.search([])
        keywords = Keyword.search([])

        return http.request.render(
            "resources_app.infrastructure_web_template",
            {
                "resources": resources,
                "themes": applicationThemes,
                "keywords": keywords,
                "universities": universities,
            }
        )
