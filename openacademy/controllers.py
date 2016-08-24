# -*- coding: utf-8 -*-
from openerp import http

# class Testmodulescaf(http.Controller):
#     @http.route('/testmodulescaf/testmodulescaf/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testmodulescaf/testmodulescaf/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testmodulescaf.listing', {
#             'root': '/testmodulescaf/testmodulescaf',
#             'objects': http.request.env['testmodulescaf.testmodulescaf'].search([]),
#         })

#     @http.route('/testmodulescaf/testmodulescaf/objects/<model("testmodulescaf.testmodulescaf"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testmodulescaf.object', {
#             'object': obj
#         })