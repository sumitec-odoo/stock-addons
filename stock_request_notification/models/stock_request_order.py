from odoo import fields, models, api


class StockRequestOrder(models.Model):
    _inherit = "stock.request.order"

    def write(self, vals):
        res = super(StockRequestOrder, self).write(vals)        
        if "state" in vals:
            for rec in self:
                message = "La solicitud de existencias se completó con exito"
                existe = self.env['mail.message'].search([('body','=',message),('res_id','=',rec.id)])
                # pasa dos veces por acá cuando se marca como "hecho"
                # por eso si ya fue agregado NO lo agrego
                if not existe and rec.state == 'done':                    
                    rec.message_post(body=message, subtype_xmlid="mail.mt_comment")
        
        return res