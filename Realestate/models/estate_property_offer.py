from odoo import api, fields, models, exceptions


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Property Offers'

    property_id = fields.Many2one('real.estate.property', string='Property')
    offer_name = fields.Char(string="Offers")
    offer_amount = fields.Float(string='Offer Amount')
    tags = fields.Many2many('real.estate.property', string='Tags')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ], string='State', default='draft')
    property_type_id = fields.Many2one(related="property_id.property_type_id", string="Property Type", store=True)

    def unlink(self, EstateProperty=None):
        for property in self:
            if property.state not in ('new', 'canceled'):
                raise exceptions.ValidationError(
                    "You cannot delete a property with the state other than 'New' or 'Canceled'.")
        return super(EstateProperty, self).unlink()
