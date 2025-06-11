from odoo import http
from odoo.http import request


class WebsitePersons(http.Controller):
    @http.route("/persons", type="http", auth="public", website=True)
    def persons_list(self, **kwargs):
        persons = (
            request.env["website.persons"].sudo().search([], limit=5, order="id desc")
        )
        return request.render(
            "website_persons.persons_list_template", {"persons": persons}
        )

    @http.route(
        "/persons/add",
        type="http",
        auth="public",
        website=True,
        methods=["GET", "POST"],
    )
    def persons_add(self, **kwargs):
        companies = request.env["res.company"].sudo().search([])
        if request.httprequest.method == "POST":
            values = {
                "first_name": kwargs.get("first_name"),
                "last_name": kwargs.get("last_name"),
                "birthday": kwargs.get("birthday"),
                "sex": kwargs.get("sex"),
                "company_id": int(kwargs.get("company_id"))
                if kwargs.get("company_id")
                else False,
            }
            request.env["website.persons"].sudo().create(values)
            return request.redirect("/persons")
        return request.render(
            "website_persons.persons_add_template", {"companies": companies}
        )
