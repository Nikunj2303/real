from odoo import fields, models


class CreateAppointmentwizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    inherite ="account"
    _description = 'Create Appointment Wizard'

    name = fields.Char(string="Name", required=True)
    property_id = fields.Many2one('real.estate.property', string='Property')
    address = fields.Char(string='Address', required=True)
    email_id = fields.Char(string='Email_id', required=True, translate=True)
    contacts = fields.Many2one("res.partner", string="Contacts")


    def action_appointment(self):
        print("Button Is clicked")

