from odoo import http

class Resources(http.Controller):
    @http.route("/resources/resource", website=True)
    def list(self, **kwargs):
        Resource = http.request.env["resources.resource"]
        resources = Resource.search([])
        return http.request.render(
            "resources_app.resource_web_template",
            {"resource": resources}
        )