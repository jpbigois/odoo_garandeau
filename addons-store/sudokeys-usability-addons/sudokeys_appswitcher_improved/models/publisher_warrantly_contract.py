# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
import werkzeug.urls
import urllib2

from odoo import models, api
from odoo.tools.translate import _
from odoo.tools import config
from odoo.tools.misc import formatLang
from datetime import datetime


_logger = logging.getLogger(__name__)

class PublisherWarrantyContract(models.AbstractModel):
    _inherit = "publisher_warranty.contract"

    @api.model
    def _get_sys_logs(self):
        """
        Utility method to send a publisher warranty get logs messages.
        """
        msg = self._get_message()
        _logger.debug('warrantly msg:%s' % msg)
        arguments = {'arg0': msg, "action": "update"}
        arguments_raw = werkzeug.urls.url_encode(arguments)

        url = config.get("publisher_warranty_url")
        _logger.debug('warrantly url:%s' % url)
        return {'messages': ''}
