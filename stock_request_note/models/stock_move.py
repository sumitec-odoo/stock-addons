# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models, api


class StockMove(models.Model):
    _inherit = "stock.move"

    note = fields.Text("Nota", compute="_compute_note")

    @api.depends("allocation_ids")
    def _compute_note(self):
        for rec in self:
            for rec2 in rec.allocation_ids:
                rec.note = rec2.stock_request_id.note
