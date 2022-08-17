# Copyright 2022 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class StockRequest(models.Model):
    _inherit = "stock.request"

    qty_available = fields.Float("Cantidad a mano", related='product_id.qty_available')
    virtual_available = fields.Float("Cantidad pronosticada", related='product_id.virtual_available')
