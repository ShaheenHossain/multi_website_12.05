# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import fields, models



class CountryState(models.Model):
    _inherit = 'res.country.state'

    city_ids = fields.One2many('res.city','state_id')

    def get_website_sale_cities(self, mode='billing'):
        return self.sudo().city_ids

