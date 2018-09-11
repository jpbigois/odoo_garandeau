# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ResCompany(models.Model):
    _inherit = 'res.company'

    legal_form = fields.Char(striing="Legal form")
    capital = fields.Monetary(string="Capital")

    @api.model
    def create(self, vals):
        if 'legal_form' in vals:
            vals.update({'legal_form': vals['legal_form'].upper()})
        return super(ResCompany, self).create(vals)

    @api.multi
    def write(self, vals):
        if 'legal_form' in vals:
            vals.update({'legal_form': vals['legal_form'].upper()})
        return super(ResCompany, self).write(vals)
