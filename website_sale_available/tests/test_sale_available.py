# License MIT (https://opensource.org/licenses/MIT).
# Copyright 2017 Kolushov Alexandr <https://github.com/KolushovAlexandr>

import eagle.tests


@eagle.tests.common.at_install(True)
@eagle.tests.common.post_install(True)
class TestUi(eagle.tests.HttpCase):
    def test_sale_available(self):
        # delay is added to be sure that all elements have been rendered properly
        self.phantom_js(
            "/",
            "eagle.__DEBUG__.services['web_tour.tour'].run('shop_sale_available', 1000)",
            "eagle.__DEBUG__.services['web_tour.tour'].tours.shop_sale_available.ready",
            login="admin",
        )
