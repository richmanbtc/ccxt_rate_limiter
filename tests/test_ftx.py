from unittest import TestCase
from ccxt_rate_limiter.ftx import ftx_limits, ftx_wrap_defs
from .wrap_object_test_helper import test_wrap_defs

class TestFtx(TestCase):
    def test_ftx(self):
        # Not covering all methods yet

        cases = [
            {
                'methods': [
                    'publicGetFundingRates',
                    'publicGetFutures',
                    'publicGetMarkets',
                    'publicGetMarketsMarketNameCandles',
                    'publicGetMarketsMarketNameOrderbook',
                    'privateDeleteOrders',
                    'privateDeleteOrdersOrderId',
                    'privateGetAccount',
                    'privateGetOrdersOrderId',
                    'privateGetPositions',
                ],
                'tag_counts': {
                    'all': 1,
                }
            },
            {
                'methods': [
                    'privatePostOrders',
                ],
                'tag_counts': {
                    'all': 1,
                    'send_order': 1,
                }
            },
        ]

        test_wrap_defs(test_case=self, limits=ftx_limits(), wrap_defs=ftx_wrap_defs(), cases=cases)
