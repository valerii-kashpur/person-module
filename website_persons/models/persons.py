from datetime import date

from odoo import api, fields, models


class Persons(models.Model):
    _name = "website.persons"
    _description = "Persons"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    full_name = fields.Char(
        string="Full Name", compute="_compute_full_name", store=True
    )
    birthday = fields.Date(string="Birthday")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    sex = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("non_binary", "Non-binary")],
        string="Sex",
    )
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        default=lambda self: self.env.company,
    )

    @api.depends("first_name", "last_name")
    def _compute_full_name(self):
        for record in self:
            record.full_name = f"{record.first_name} {record.last_name}"

    @api.depends("birthday")
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birthday:
                birth_date = fields.Date.from_string(record.birthday)
                record.age = (
                    today.year
                    - birth_date.year
                    - ((today.month, today.day) < (birth_date.month, birth_date.day))
                )
            else:
                record.age = 0
