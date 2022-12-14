from odoo import fields, models, api, _


class StockRequest(models.Model):
    _inherit = "stock.request"

    @api.model
    def create(self,vals):
        res = super(StockRequest, self).create(vals)

        # Cuando se crea automáticamente pone como seguidor al creador
        # con este código lo quito
        follower_record = self.env["mail.followers"].search([('res_model', '=', "stock.request"),
                                                    ('res_id', '=', res.id)])
        follower_record.sudo().write({'subtype_ids': [(3, 1,_)]})

                
        return res

