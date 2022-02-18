from unittest import TestCase
from ccxt_rate_limiter.kraken import kraken_limits, kraken_wrap_defs
from .wrap_object_test_helper import test_wrap_defs

class TestKraken(TestCase):
    def test_kraken(self):
        # Not covering all methods yet

        cases = [
            {
                'methods': [
                    'publicGetOHLC',
                ],
                'tag_counts': {
                    'public': 1,
                }
            },

        ]

        test_wrap_defs(test_case=self, limits=kraken_limits(), wrap_defs=kraken_wrap_defs(), cases=cases)
