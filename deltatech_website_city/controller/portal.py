import math
import re

from werkzeug import urls

from eagle import fields as eagle_fields, tools, _
from eagle.exceptions import ValidationError, AccessError, MissingError, UserError
from eagle.http import content_disposition, Controller, request, route
from eagle.tools import consteq
from eagle.addons.portal.controllers.portal import pager as portal_pager, CustomerPortal
from eagle import fields, http, tools, _

class CustomerPortalCity(CustomerPortal):

    MANDATORY_BILLING_FIELDS = ["name", "phone", "email", "street", "city", "country_id"]
    OPTIONAL_BILLING_FIELDS = ["zipcode", "state_id", "vat", "company_name", "city_id"]

    def _prepare_portal_layout_values(self):
        values = super(CustomerPortalCity, self)._prepare_portal_layout_values()
        # cities = request.env['res.city'].sudo().search([])
        # values['cities'] = cities
        values['city_id'] =  request.env.user.partner_id.city_id.id
        return values

    @http.route(['/shop/state_infos/<model("res.country.state"):state>'], type='json', auth="public", methods=['POST'], website=True)
    def country_infos(self, state, mode, **kw):
        return dict(
            cities=[(st.id, st.name, st.zipcode or '') for st in state.get_website_sale_cities(mode=mode)],
        )