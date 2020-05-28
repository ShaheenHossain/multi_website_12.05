# -*- coding: utf-8 -*-
# Part of Eagle. See LICENSE file for full copyright and licensing details.
import eagle.tests


@eagle.tests.common.at_install(False)
@eagle.tests.common.post_install(True)
class TestUi(eagle.tests.HttpCase):
    def run_tour(self, login=None):
        self.phantom_js(
            "/",

            "eagle.__DEBUG__.services['web_tour.tour']"
            ".run('shop_buy_product')",

            "eagle.__DEBUG__.services['web_tour.tour']"
            ".tours.shop_buy_product.ready",

            login=login
        )

    # keep test numbering from module website_sale.
    # Test 01 is not needed in this module
    def test_02_admin_checkout(self):
        self.run_tour("admin")

    def test_03_demo_checkout(self):
        self.run_tour("demo")

    def test_04_public_checkout(self):
        self.run_tour()
