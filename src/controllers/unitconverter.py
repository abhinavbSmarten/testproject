from odoo import http
from odoo.http import request

class UnitConverter(http.Controller):
    @http.route('/unit-converter', type='http', auth='public', website=True)
    def converter(self, **kw):
        
        return request.render('src.unitcon', {})
