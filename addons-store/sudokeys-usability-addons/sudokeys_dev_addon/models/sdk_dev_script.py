from odoo import models,fields,api

class SdkDevScript(models.Model):
    _name = "sdk.dev.script"

    @api.model
    def _clean_script(self):
        # Delete all outgoiing mail servers
        outgoing_servers = self.env['ir.mail_server'].search([])
        if outgoing_servers:
            outgoing_servers.unlink()
        # Delete all incoming mail servers
        incoming_servers = self.env['fetchmail.server'].search([])
        if incoming_servers:
            incoming_servers.unlink()
        # Delete odoo enterprise code from system parameters
        code = self.env['ir.config_parameter'].search([('key','=','database.enterprise_code')])
        if code:
            code.unlink()
