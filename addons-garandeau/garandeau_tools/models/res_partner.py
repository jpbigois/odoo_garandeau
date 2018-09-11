# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class PartnersGarandeau(models.Model):
	# ------------------------------------------
    # CHAMPS DE LA CLASSE MODEL A DEFINIR
    # ------------------------------------------

	_inherit = 'res.partner'

	siret = fields.Char( index=True )
	nic = fields.Char( index=True )
