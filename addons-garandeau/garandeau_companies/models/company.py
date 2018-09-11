# -*- coding: utf-8 -*-

import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)


class societesGarandeau(models.Model):
    # ------------------------------------------
    # CHAMPS DE LA CLASSE MODEL A DEFINIR
    # ------------------------------------------

    _inherit = 'res.company'

    codesociete = fields.Integer(string="Code interne de la societe")

    _sql_constraints = [
        ('codesociete_unique', 'unique(codesociete)', 'Une societe a deja ce numero')
    ]