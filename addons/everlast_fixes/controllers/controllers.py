# -*- coding: utf-8 -*-
from odoo import http


class EverlastFixes(http.Controller):
    @http.route('/everlast_fixes/everlast_fixes/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/everlast_fixes/everlast_fixes/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('everlast_fixes.listing', {
            'root': '/everlast_fixes/everlast_fixes',
            'objects': http.request.env['everlast_fixes.everlast_fixes'].search([]),
        })

    @http.route('/everlast_fixes/everlast_fixes/objects/<model("everlast_fixes.everlast_fixes"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('everlast_fixes.object', {
            'object': obj
        })
