from odoo import models, fields, api

class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Simple Model Cristi'

    name = fields.Char(string='Name', required=True)
    value = fields.Integer(string='Value')
    description = fields.Text(string='Description')
    auto_reload_test = fields.Char(string='Auto Reload Test')
# Test auto-reload Sat Nov 15 03:19:46 PM UTC 2025
# Auto-update: Sat Nov 15 03:24:02 PM UTC 2025
