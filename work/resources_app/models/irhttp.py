from odoo import models, http, SUPERUSER_ID

class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    @classmethod
    def _auth_method_my_api_key(cls):
        api_key = http.request.httprequest.headers.get("Authorization")
        if not api_key or (api_key != "123456"):
            return 

        user = http.request.env['res.users'].sudo(SUPERUSER_ID).search([('login', '=', 'admin')])
        http.request.uid = user.id


        #RIGHT CODE -->
        #user_id = http.request.env["res.users.apikeys"]._check_credentials(
        #    scope="rpc", key=api_key
        #)

        #if not user_id:
        #    return
        #
        #http.request.uid = user_id
