{
    "name": "Website Persons",
    "version": "1.0",
    "summary": "Manage persons and display them on website",
    "depends": ["website", "base"],
    "data": [
        "security/ir.model.access.csv",
        "views/persons_views.xml",
        "views/website_templates.xml",
    ],
    "installable": True,
    "auto_install": False,
}
