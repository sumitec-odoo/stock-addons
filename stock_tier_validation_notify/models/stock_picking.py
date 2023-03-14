# Copyright 2021 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields

class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = ['stock.picking', 'tier.validation']

    user_requesting_review = fields.Many2one('res.users',string="Usuario que solicita la revisión")

    def _notify_accepted_reviews(self):
        super(StockPicking,self)._notify_accepted_reviews()
        notification_ids = []
        notification_ids.append((0,0,{
                'res_partner_id':self.user_requesting_review.partner_id.id}))        
        subtype_id = self.env['ir.model.data']._xmlid_to_res_id('mail_mt_note')
        self.message_post(
            body='Se aprobo su pedido de revisión!', 
            message_type='notification',
            notification_ids=notification_ids,
            subtype_id=subtype_id)

    def request_validation(self):
        self.user_requesting_review = self.env.user
        super(StockPicking,self).request_validation()