# -*- coding: utf-8 -*-

import base64
import urllib.request
import urllib.parse
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from google_images_search import GoogleImagesSearch

class ResPartnerInherit(models.Model):

    _inherit = 'res.partner'

    linkedin = fields.Char(string="LinkedIn", widget="url")
    linkedin_confirm = fields.Boolean(string="")

    @api.model 
    def update_partner_image(self):
        if self.linkedin != False:
            # Set up the Google Images Search API
            gis = GoogleImagesSearch('AIzaSyCbQYP6MlcqqdEVaJZaGfxVBQ8Ed99cZU4', '57f3b43d93d414785')

            # Define the search parameters
            search_params = {
                'q': 'media.licdn.com AND ' + urllib.parse.unquote(self.linkedin).split("/in/")[1].strip("/"),
                'imgType': 'photo'
            }

            # Send the search request and get the results
            gis.search(search_params=search_params)
            results = gis.results()

            # Get the URL of the first image result
            if results:
                first_result = results[0]
                image_url = first_result.url
                image_data = urllib.request.urlopen(image_url).read()
                if("media.licdn.com" in image_url):
                    self.write({
                        'image_1920': base64.b64encode(image_data),
                    })
    

    @api.constrains('linkedin', 'linkedin_confirm')
    def _check_linkedin(self):
        for record in self:
            if not record.linkedin_confirm and record.linkedin:
                raise ValidationError("Please give permissions to use LinkedIn information")
            else:
                record.update_partner_image()
