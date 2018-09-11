# -*- coding: utf-8 -*-
from odoo import http


class Garandeau(http.Controller):
    @http.route('/ws/invoice', auth='public', type='json', csrf=False, methods=['POST'])
    def index(self, **kw):
        print kw
        return kw
