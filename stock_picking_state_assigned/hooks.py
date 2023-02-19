from odoo import api, SUPERUSER_ID

# def post_init_hook(cr, registry):
# addons-OCA/e-commerce/setup/website_sale_secondary_unit/odoo/addons/website_sale_secondary_unit/hooks.py

    # cr.execute("""
    #     UPDATE stock_picking
    #     SET state_detail_id= 11
    #     WHERE state_detail_id IS NULL;
    # """)

# addons-OCA/account-analytic/setup/account_analytic_sequence/odoo/addons/account_analytic_sequence/hooks.py
def post_init_hook(cr, registry):
    
    env = api.Environment(cr, SUPERUSER_ID, {})

    state_detail_id = env['stock.picking']._default_state().id
    
    # import pdb; pdb.set_trace()

    # cr.execute("""
    #     UPDATE stock_picking
    #     SET state_detail_id= {0}
    #     WHERE state_detail_id IS NULL;
    # """.format(state_detail_id))

    cr.execute("""
        UPDATE stock_picking
        SET state_detail_id= {0}
        FROM stock_picking sp
        INNER JOIN stock_picking_type spt on sp.picking_type_id = spt.id
        WHERE sp.state_detail_id IS NULL and spt.code = 'outgoing';
    """.format(state_detail_id))