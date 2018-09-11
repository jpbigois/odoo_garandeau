# -*- coding: utf-8 -*-

from odoo import models, api
import logging
_logger = logging.getLogger(__name__)


class mail_thread(models.AbstractModel):
    _name = 'mail.thread'
    _inherit = 'mail.thread'

    @api.multi
    @api.returns('self', lambda value: value.id)
    def message_post(self, body='', subject=None, message_type='notification',
                     subtype='mail.mt_comment', parent_id=False, attachments=None,
                     content_subtype='html', **kwargs):
        res = {}
        email_template_obj = self.env['mail.template']
        self.ensure_one()
        email_template_ids = email_template_obj.search([('model', '=', str(self._name)), ('name', 'ilike', '[' + message_type + ']')], limit=1)
        if email_template_ids:
            return self.with_context(mail_notrack=True).message_post_with_template(email_template_ids.id)
        else:
            return super(mail_thread, self).message_post(body, subject, message_type, subtype, parent_id, attachments, content_subtype, **kwargs)
