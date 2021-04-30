# © 2021 onDevelop.SA
# ondevelop.sa@gmail.com
# Createed by: Idelis Gé Ramírez

from odoo import models, fields, api, _
from datetime import datetime


# class partner_rank(models.Model):
#     _name = 'partner_rank.partner_rank'
#     _description = 'partner_rank.partner_rank'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
