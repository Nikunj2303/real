from odoo import models, fields, api, exceptions

class RealEstateProperty(models.Model):
    _inherit = 'real.estate.property'

    def button_mark_sold(self):
        for record in self:
            price = record.selling_price
            quantity = 1
            admin_fee = 100.00
            journal = self.env['account.journal'].search([("type", "=", "sale")])
            writeoff_move = self.env['account.move'].with_context(default_move_type='out_invoice').create({
                'partner_id': record.buyer_id.id,
                'journal_id': journal.id,
                "invoice_line_ids": [
                    (
                        0,
                        0,
                        {
                            'name': 'Selling Price',
                            'quantity': quantity,
                            'price_unit': price * 0.06,

                        },
                    )
                ],
            })
        return super().button_mark_sold()
