from odoo import models, fields, api

class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Simple Model Cristi'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # ✅ aici adaugi thread

    name = fields.Char(string='Name', required=True, tracking=True, default="test")
    value = fields.Integer(string='Value')
    description = fields.Text(string='Description')
    auto_reload_test = fields.Char(string='Auto Reload Test')
    text_input = fields.Char(string="Text Input")
