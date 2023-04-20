# -*- coding: utf-8 -*-
{
    'name': "Resources App",
    'summary': "Manage, access and share of the university resources",
    'author': "Unite",
    'license': "AGPL-3",
    'website': "https://metacampus.unite-university.eu/",
    'version': '15.0.1.0.0',
    'depends': ['base', 'website'],
    'application': True,
    'category': "Services",
    'data': [
        "security/resources_security.xml",
        "security/ir.model.access.csv",
	    "views/resources_menu.xml",
        "views/infrastructure.xml",
        "views/capacity.xml",
        "views/web/infrastructure_web_template.xml",
        "views/web/infrastructure_web_menu.xml",
        "views/web/infrastructure_list.xml",
        "demo/universities.xml",
        "demo/themes.xml",
        "demo/keywords.xml",
        "demo/contacts.xml",
        "demo/demo.xml",
        "reports/resource_infrastructure_report.xml",
    ],
    'assets': {
        "web.assets_frontend": {
            "resources_app/static/src/css/resource_web_template.css",
            "resources_app/static/src/js/resource_web_template.js",
            
        }
    }
}
