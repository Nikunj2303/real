from odoo import models, fields, api

class PropertyTag(models.Model):
    _name = 'property.tag'
    _description = 'Property Tag'

    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color")
