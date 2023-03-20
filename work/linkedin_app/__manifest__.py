# -*- coding: utf-8 -*-
{
"name": "LinkedIn App",
"license": "AGPL-3",
"description": "Add linkedIn field in Contact and add profile picture from it",
"author": "Alba Roma",
'depends': [
    "contacts",
    "base"
],
"application": False,
"installable": True,
"auto_install": True,
"data": [
	"views/partner_views.xml",
    "data/cron.xml"
]
}
