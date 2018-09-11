# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ResUsers(models.Model):
    _inherit = 'res.users'

    customer = fields.Boolean(related='partner_id.customer', default=False)

    @api.model
    def create(self, vals):
        if vals.get('groups_id',False) == [(6,0,[])]:
            vals.update({'customer': True})
        return super(ResUsers, self).create(vals)
