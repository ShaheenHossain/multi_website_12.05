from eagle import http
from eagle.http import request

from eagle.addons.website_sale.controllers.main import WebsiteSale as controller


class WebsiteSale(controller):
    @http.route()
    def shop(self, page=0, category=None, search="", ppg=False, **post):
        request.context = dict(request.context, search_tags=search)
        return super(WebsiteSale, self).shop(page, category, search, ppg, **post)
