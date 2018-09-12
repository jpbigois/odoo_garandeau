# -*- coding: utf-8 -*-
from odoo import http
import logging
from odoo.http import request

_logger = logging.getLogger(__name__)

class Garandeau(http.Controller):

    @http.route('/ws/createInvoice', auth='public', csrf=False, type="json", methods=['POST'])
    def index(self, **kw):
        print kw
        facture = kw["facture"]
        mode = kw["mode"]

        _logger.info("INFO : %s" %facture)

        print("CLI_%s" %facture["_codeClient"])
        partner = request.env["res.partner"].sudo().search([("ref","=","CLI_%s" %facture["_codeClient"])])

        if(partner.id == False):
            print("Client \"CLI_%s\" non trouvé dans odoo !" %facture["_codeClient"])
            return False

        invoiceLine = []

        for line in facture["pageFacture"]:
            # TODO : A voir pour le filtre de produit (_ pas prit en compte ?)
            print("%s_%s" %(mode,line["_codeArticle"]))
            product = request.env["product.product"].sudo().search([("default_code","like","%s_%s" %(mode,line["_codeArticle"]))], limit=1)
            invoiceLine.append((0,0,{
                "product_id":product.id,
                "account_id":product.property_account_income_id and product.property_account_income_id.id or 1335,
                "name":line["_libArticle"],
                "quantity":line["_quantite"],
                "price_unit": line["_prixUnit"],

                #TODO
                #_codeTVA
            }))

        print("codeSociete : %i" %facture["_soc"])
        societe = request.env["res.company"].sudo().search([("codesociete","=", "%i" %facture["_soc"])])
        journal = request.env["account.journal"].sudo().search([("ref", "=", "CLI_%s" % facture["_codeClient"])])

        invoice = request.env["account.invoice"].sudo().create({
            "partner_id":partner.id,
            "journal_id":8,
            "company_id":11,
            "account_id":997,
            "invoice_line_ids":invoiceLine,
            "type":"out_invoice"
        })

        print "On est pas planté !"

        # TODO : if not alert -> validation facture

        invoice.action_invoice_open()

        return "Hello, world"

    # @http.route('/garandeau/garandeau/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('garandeau.listing', {
    #         'root': '/garandeau/garandeau',
    #         'objects': http.request.env['garandeau.garandeau'].search([]),
    #     })

#     @http.route('/garandeau/garandeau/objects/<model("garandeau.garandeau"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('garandeau.object', {
#             'object': obj
#         })