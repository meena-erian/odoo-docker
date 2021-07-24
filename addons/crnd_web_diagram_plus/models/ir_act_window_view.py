from odoo import fields, models


class IrActionsActWindowView(models.Model):
    _inherit = 'ir.actions.act_window.view'

    view_mode = fields.Selection(
        selection_add=[('diagram_plus', 'DiagramPlus')],
        ondelete={'diagram_plus': 'cascade'},
    )
