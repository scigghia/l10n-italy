# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from openerp import models


class WizardExportFatturapa(models.TransientModel):
    _inherit = "wizard.export.fatturapa"

    def setFatturaElettronicaBody(self, invoice, body):
        rel_docs_model = self.env['fatturapa.related_document_type']
        if invoice.partner_id.fatturapa_sale_order_data:
            # if sale_order refer to the whole invoice create only 1 rel doc
            if invoice.picking_ids and set(self.env['sale.order'].search([
                ('name', 'in', invoice.picking_ids.mapped('origin'))]).mapped(
                'client_order_ref')) == 1 or \
                    len(set(invoice.invoice_line.mapped('origin'))) == 1:
                # check if already present ref for this invoice
                existing_rel_docs = rel_docs_model.search([
                    ('invoice_id', '=', invoice.id),
                    ('type', '=', 'order')
                ])
                if existing_rel_docs:
                    existing_rel_docs.unlink()
                doc_data = self.prepareRelDocsLine(
                    invoice, invoice.invoice_line[0], 'order', True)
                if doc_data:
                    rel_docs_model.create(doc_data)
            else:
                for line in invoice.invoice_line:
                    # unlink related docs for this invoice line
                    existing_rel_docs = rel_docs_model.search([
                        ('invoice_line_id', '=', line.id),
                    ])
                    if existing_rel_docs:
                        existing_rel_docs.unlink()
                    doc_data = self.prepareRelDocsLine(
                        invoice, line, 'order')
                    if doc_data:
                        rel_docs_model.create(doc_data)
        res = super(WizardExportFatturapa, self).setFatturaElettronicaBody(
            invoice, body)
        return res

    def prepareRelDocsLine(self, invoice, line, type, whole=False):
        res = False
        sale_order_name = False
        if line.origin:
            # if invoiced from picking, get sale_order from picking
            for picking in invoice.picking_ids:
                if picking.name == line.origin:
                    sale_order_name = picking.origin
                    break
            # else use origin directly
            if not sale_order_name:
                sale_order_name = line.origin
            order = self.env['sale.order'].search(
                [('name', '=', sale_order_name)])
            if order:
                res = {
                    'type': type,
                    'name': order.client_order_ref or order.name,
                    'invoice_line_id': line.id if not whole else False,
                    'invoice_id': invoice.id if whole else False,
                    'date': order.date_order,
                }
        return res
