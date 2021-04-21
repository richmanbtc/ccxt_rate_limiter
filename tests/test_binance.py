from unittest import TestCase
from ccxt_rate_limiter.binance import binance_limits, binance_wrap_defs
from .wrap_object_test_helper import test_wrap_defs

class TestBinance(TestCase):
    def test_binance(self):
        # Not covering all methods yet

        cases = [
            {
                'methods': [
                    'publicGetExchangeInfo',
                ],
                'tag_counts': {
                    'all': 1,
                }
            },
            {
                'methods': [
                    'privatePostOrder',
                ],
                'tag_counts': {
                    'all': 1,
                    'send_order': 1,
                }
            },
        ]

        test_wrap_defs(test_case=self, limits=binance_limits(), wrap_defs=binance_wrap_defs(), cases=cases)
