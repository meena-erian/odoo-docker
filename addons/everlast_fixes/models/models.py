# -*- coding: utf-8 -*-

from odoo import models, fields, api


class patient(models.Model):
    _name = 'everlast_fixes.patient'
    # _inherit = [
    #     'res.partner'
    # ]
    _description = """
        Each patient record represents one and only one individual. 
        However, one patient might have multiple the same contact information
        (for example a husband and a wife) and one patient might have multiple
        contact information.
        """
    mrn = fields.Char(compute="_compute_mrn", store=True, string="Medical Record Number")
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    national_id = fields.Char(string="National Id Number")
    #chartnumber = fields.Integer(string="Medical Record Number")
    tags = fields.Many2many('generic.tag', string="Tags")
    #Contacts = fields.Many2one('res.partner', string="Contact Info")
    #contact_info = fields.Many2one("res.partner", string="Contact Info")

    def _compute_mrn(self):
        for record in self:
            record.mrn = record.id

# class everlast_fixes(models.Model):
#     _name = 'everlast_fixes.everlast_fixes'
#     _description = 'everlast_fixes.everlast_fixes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
