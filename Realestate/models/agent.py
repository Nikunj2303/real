from odoo import models, fields


class Agent(models.Model):
    _name = 'real.estate.agent'
    _description = 'Real Estate Agent'

    name = fields.Char(string='Agent Name', required=True)
    agents = fields.Many2many('real.estate.agent', string='Subagents', relation='agent_agent_rel', column1='agent_id',
                              column2='subagent_id')



