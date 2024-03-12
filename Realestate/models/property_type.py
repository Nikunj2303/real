from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"

    name = fields.Char(string="Type Name")
    property_ids = fields.One2many('real.estate.property', 'property_type_id', string="Properties")
    property_type_id = fields.Many2one('real.estate.property', string="Property Type")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
