# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerRank(http.Controller):
#     @http.route('/partner_rank/partner_rank/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_rank/partner_rank/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_rank.listing', {
#             'root': '/partner_rank/partner_rank',
#             'objects': http.request.env['partner_rank.partner_rank'].search([]),
#         })

#     @http.route('/partner_rank/partner_rank/objects/<model("partner_rank.partner_rank"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_rank.object', {
#             'object': obj
#         })
