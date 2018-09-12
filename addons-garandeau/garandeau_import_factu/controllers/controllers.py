# -*- coding: utf-8 -*-
from odoo import http
import logging
from odoo.http import request

_logger = logging.getLogger(__name__)

class Garandeau(http.Controller):

    @http.route('/ws/createInvoice', auth='public', csrf=False, type="json", methods=['POST'])
    def index(self, **kw):
        facture = kw["facture"]
        mode = kw["mode"]

        _logger.info("INFO : %s" %facture)

        #partner = request.env["res.partner"].sudo().search([("ref","=","%s" %facture["_codeClient"])])
        partner = request.env["res.partner"].sudo().search([("ref","=","99361")])
        company = request.env["res.company"].sudo().search([("codesociete","=","%s" %facture["_soc"])])

        if not (partner and company) :
            print("Client \"CLI_%s\" non trouvé dans odoo !" %facture["_codeClient"])
            return False

        invoiceLine = []

        for line in facture["pageFacture"]:
            product = request.env["product.product"].sudo().search([("default_code","like","%s_%s" %(mode,line["_codeArticle"]))], limit=1)
            tax = request.env['account.tax'].sudo().search([('company_id', '=', company.id), ('code_it7', '=', line['_codeTVA'])])
            invoiceLine.append((0,0,{
                "product_id":product and product.id or False,
                "account_id":product.property_account_income_id and product.property_account_income_id.id or 4192,
                "name":line["_libArticle"],
                "quantity":line["_quantite"],
                "price_unit": line["_prixUnit"],
                "invoice_line_tax_ids" : [(6, None,tax.ids)],
            }))

        date = facture["_date"].split('/')
        date_due = facture["_echeance"].split('/')
        journal = request.env["account.journal"].sudo().search([("type", "=", "sale"),("company_id", "=", company.id)])
        invoice = request.env["account.invoice"].sudo().create({
            "number_invoice_it7":facture["_num"],
            "date_invoice":date[2]+'-'+date[1]+'-'+date[0],
            "date_due":date_due[2]+'-'+date_due[1]+'-'+date_due[0],
            "partner_id":partner.id,
            "journal_id":journal.id,
            "company_id":company.id,
            "account_id":partner.property_account_receivable_id.id,
            "invoice_line_ids":invoiceLine,
            "type":"out_invoice"
        })


        # TODO : if not alert -> validation facture

        #request.env.cr.commit()
        #invoice.action_invoice_open()


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
