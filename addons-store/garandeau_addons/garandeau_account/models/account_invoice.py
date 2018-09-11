# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import except_orm, UserError, Warning, RedirectWarning
from odoo.tools import float_compare
import odoo.addons.decimal_precision as dp
import logging

_logger = logging.getLogger(__name__)
class AccountInvoice(models.Model):
    _inherit = "account.invoice"
    _name = "account.invoice"

    number_invoice_it7 = fields.Char(string='IT7 invoice number', index=True,
        readonly=True, states={'draft': [('readonly', False)]}, copy=False,
        help="Technical field holding the number given to the invoice, in IT7.")

    _sql_constraints = [
        ('it7_number_uniq', 'unique(number_invoice_it7, company_id, journal_id, type)', 'IT7 Invoice Number must be unique per Company!'),
    ]
    
    
    @api.multi
    def action_invoice_open(self):
        # lots of duplicate calls to action_invoice_open, so we remove those already open
        to_open_invoices = self.filtered(lambda inv: inv.state in  ['proforma2', 'draft'])
        for inv in to_open_invoices:
            if inv.transmit_method_code != 'fr-chorus' or inv.move_name:
                continue
            if not inv.number_invoice_it7:
                raise UserError(_("Invoice must be have an IT7 number invoice."))
            inv.move_name = inv.number_invoice_it7
        return super (AccountInvoice, self).action_invoice_open()