# -*- coding: utf-8 -*-
{
    'name': "Resources App",
    'summary': "Manage, access and share of the university resources",
    'author': "Unite",
    'license': "AGPL-3",
    'website': "https://metacampus.unite-university.eu/",
    'version': '15.0.1.0.0',
    'depends': ['base'],
    'application': True,
    'category': "Services",
    "data": [
        "security/resources_security.xml",
        "security/ir.model.access.csv",
	    "views/resources_menu.xml",
        "views/resource.xml"
    ],
}
