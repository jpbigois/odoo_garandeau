# -*- coding: utf-8 -*-
##############################################################################
#
#    L10n FR Fix Thousands Separator module for Odoo
#    Copyright (C) 2016 Akretion (http://www.akretion.com)
#    Copyright (C) 2016 Sudokeys
#
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#    @contributor Nicolas JEUDY <nicolas@sudokeys.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import models, api


class ResLang(models.Model):
    _inherit = 'res.lang'

    @api.model_cr
    def init(self):
        narrow_no_break_space = u'\u00A0'
        self._cr.execute(
            "UPDATE res_lang SET thousands_sep=%s, grouping='[3,3,3,-1]' "
            "WHERE code='fr_FR'", (narrow_no_break_space, ))
        self._cr.execute(
            "UPDATE res_lang SET grouping='[3,3,3,-1]' WHERE code='en_US'")
        return True
