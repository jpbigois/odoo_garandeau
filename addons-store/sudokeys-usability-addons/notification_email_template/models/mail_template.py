# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class mail_template(models.Model):

    _inherit = 'mail.template'

    company_id = fields.Many2one(string=u"Société", comodel_name="res.company")
