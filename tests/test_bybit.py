from unittest import TestCase
from ccxt_rate_limiter.bybit import bybit_limits, bybit_wrap_defs
from .wrap_object_test_helper import test_wrap_defs

class TestBybit(TestCase):
    def test_bybit(self):
        # Not covering all methods yet

        cases = [
            {
                'methods': [
                    'publicGetKlineList',
                    'publicGetTickers',
                ],
                'tag_counts': {
                    'get': 1,
                }
            },
            {
                'methods': [
                    'privatePostOrderCreate',
                    'privatePostOrderCancel',
                    'privatePostStopOrderCancel',
                ],
                'tag_counts': {
                    'post': 1,
                    'order': 1,
                }
            },
            {
                'methods': [
                    'privatePostOrderCancelAll',
                    'privatePostStopOrderCancelAll',
                ],
                'tag_counts': {
                    'post': 1,
                    'order': 10,
                }
            },
            {
                'methods': [
                    'privateGetOrder',
                ],
                'tag_counts': {
                    'get': 1,
                    'get_order': 1,
                }
            },
            {
                'methods': [
                    'privateGetPositionList',
                    'privateGetWalletBalance',
                ],
                'tag_counts': {
                    'get': 1,
                    'get_position': 1,
                }
            },
        ]

        test_wrap_defs(test_case=self, limits=bybit_limits(), wrap_defs=bybit_wrap_defs(), cases=cases)
