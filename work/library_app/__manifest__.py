# -*- coding: utf-8 -*-
{
    "name": "Library Management",
	"summary": "Manage library catalog and book lending.",
	"author": "Daniel Reis",
	"license": "AGPL-3",
    "website": "https://github.com/PacktPublishing"
                "/Odoo-15-Development-Essentials",
	"version": "15.0.1.0.0",
	"depends": ["base"],
    "application": True,
	"data": [
		"security/library_security.xml",
		"views/library_menu.xml",		
	],
}
