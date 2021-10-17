from unittest import TestCase
from ccxt_rate_limiter.okex import okex_limits, okex_wrap_defs
from .wrap_object_test_helper import test_wrap_defs

class TestOkex(TestCase):
    def test_okex(self):
        # Not covering all methods yet

        cases = [
            {
                'methods': [
                    'publicGetMarketTrades',
                ],
                'tag_counts': {
                    'all': 1,
                }
            },
            {
                'methods': [
                    'privateGetAccountPositions',
                ],
                'tag_counts': {
                    'all': 1,
                    'get_position': 1,
                }
            },
            {
                'methods': [
                    'privateGetTradeOrder',
                ],
                'tag_counts': {
                    'all': 1,
                    'get_order': 1,
                }
            },
            {
                'methods': [
                    'privateGetTradeFillsHistory',
                ],
                'tag_counts': {
                    'all': 1,
                    'get_fill': 1,
                }
            },

        ]

        test_wrap_defs(test_case=self, limits=okex_limits(), wrap_defs=okex_wrap_defs(), cases=cases)
