from odoo import fields, models


class ModulCristi(models.Model):
    _name = 'modul.cristi'
    _description = 'Înregistrare Modul Cristi'

    name = fields.Char(string='Nume', required=True)
    description = fields.Text(string='Descriere')
