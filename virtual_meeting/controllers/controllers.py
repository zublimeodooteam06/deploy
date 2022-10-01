# -*- coding: utf-8 -*-
# from odoo import http


# class VirtualMeeting(http.Controller):
#     @http.route('/virtual_meeting/virtual_meeting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/virtual_meeting/virtual_meeting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('virtual_meeting.listing', {
#             'root': '/virtual_meeting/virtual_meeting',
#             'objects': http.request.env['virtual_meeting.virtual_meeting'].search([]),
#         })

#     @http.route('/virtual_meeting/virtual_meeting/objects/<model("virtual_meeting.virtual_meeting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('virtual_meeting.object', {
#             'object': obj
#         })
