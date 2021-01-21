# -*- coding: utf-8 -*-

from odoo import models, fields, api


class olamundo(models.Model):
    _name = "olamundo.olamundo"
    _description = "Test olamundo"

    name = fields.Char(string = "OLA MUNDO")

# class odoo_holamundo(models.Model):
#     _name = 'odoo_holamundo.odoo_holamundo'
#     _description = 'odoo_holamundo.odoo_holamundo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
