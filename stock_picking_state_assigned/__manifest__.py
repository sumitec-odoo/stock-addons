# Copyright 2021 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "stock_picking_state_assigned",
    "summary": "",
    "version": "15.0.1.1.0",
    "category": "Stock",
    "website": "https://github.com/juanpgarza/stock-addons",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": [
            "stock", 
            "stock_picking_state", 
            "sale_order_type_invoice_policy",
        ],
    "data": [
        'data/data.xml',
        'views/stock_picking_views.xml',
        ],
    "installable": False,
}
