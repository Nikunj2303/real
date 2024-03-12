from odoo import models, fields, api, exceptions


class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'
    _order = "id desc, sequence"
    _rec_name = 'name'

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Name must be unique')
    ]

    name = fields.Char(string='Estate Name', required=True, translate=True)
    number_of_months = fields.Integer(string='Months', required=1)
    active = fields.Boolean(string='Active', default=True)
    sequence = fields.Integer(string='Sequence', default=10)
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability')
    expected_price = fields.Float(string='Expected Price')
    best_price = fields.Float(string='Best_price')
    tag_ids = fields.Float(string='Tag Ids')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms')
    facades = fields.Integer(string='Facades')
    contacts = fields.Many2one("res.partner", string="Contacts")
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden', default=False)
    garden_area = fields.Integer(string='Garden Area')
    living_area = fields.Integer(string='Living Area')
    total_area = fields.Integer(string='Total Area', compute='_compute_total_area', store=True)
    garden_orientation = fields.Selection(
        selection=[
            ("N", "North"),
            ("S", "South"),
            ("E", "East"),
            ("W", "West"),
        ],
        string="Garden Orientation", )
    description = fields.Text(string='Description')
    offers_ids = fields.One2many('estate.property.offer', "property_id", string='Property Offers')
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    seller_id = fields.Many2one("res.partner", string="Seller")
    agents = fields.Many2many('real.estate.agent', string='Agents')
    property_type = fields.Selection([
        ('Duplex', 'Duplex'),
        ('Villa', 'Villa'),
        ('Bunglow', 'Bunglow'),
        ('Apartment', 'Apartment'),
    ], string='Property Type')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('canceled', 'Canceled'),
        ('sold', 'Sold'),
    ], string='Status', default='draft', track_visibility='onchange')
    property_ids = fields.Many2one('estate.property.type', string="Property Type")
    property_type_id = fields.Many2one('estate.property.type', string="Property Type")
    properties = fields.Many2many('estate.property.agent', 'property_agent_rel', 'property_id', 'agent_id',
                                  string="Properties")


    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'North'
        else:
            self.garden_area = False
            self.garden_orientation = False

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            if record.living_area and record.garden_area:
                record.total_area = record.living_area + record.garden_area
            elif record.living_area:
                record.total_area = record.living_area
            elif record.garden_area:
                record.total_area = record.garden_area
            else:
                record.total_area = 0

    def action_do_something(self):
        for record in self:
            record.name = "Something"
        return True

    def mark_sold(self):
        self.write({'state': 'sold'})

    def mark_canceled(self):
        self.write({'state': 'canceled'})

    def button_mark_sold(self):
        self.mark_sold()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    def button_mark_canceled(self):
        self.mark_canceled()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    @api.constrains('state')
    def _check_property_deletion(self):
        for record in self:
            if record.state not in ('New', 'Canceled'):
                continue
            else:
                raise exceptions.ValidationError(
                    "You cannot delete a property with state other than 'New' or 'Canceled'.")

    def action_done(self):
        print("Property Details Show")

    # def action_sold(self):
    #     res = super().action_sold()
    #
    #     # Create a customer invoice
    #     invoice = self.env['account.move'].create({
    #         'partner_id': self.buyer_id.id,  # Use the property's buyer as the customer
    #         'move_type': 'out_invoice',  # Customer Invoice
    #         'journal_id': self.env['account.journal'].search([('type', '=', 'sale')], limit=1).id,
    #         # Use a suitable sales journal
    #     })
    #
    #     self.env['account.move.line'].create({
    #         'name': 'Selling Price',
    #         'quantity': 1,
    #         'price_unit': self.selling_price * 0.06,  # 6% of the selling price
    #         'move_id': invoice.id,
    #     })
    #
    #     self.env['account.move.line'].create({
    #         'name': 'Administrative Fees',
    #         'quantity': 1,
    #         'price_unit': 100.00,  # Additional 100.00 administrative fees
    #         'move_id': invoice.id,
    #     })
    #
    #     return res
