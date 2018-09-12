# -*- coding: utf-8 -*-

import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class it7CodeTax(models.Model):
    _inherit = 'account.tax'
    code_it7 = fields.Char(string="Code IT7")

