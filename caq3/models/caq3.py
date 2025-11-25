# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CAQ3(models.Model):
    _name = 'caq3.caq3'
    _description = 'CAQ3 Demo Model'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
