from unittest import TestCase
from ccxt_rate_limiter import scale_limits

class TestScaleLimits(TestCase):
    def test_scale_limits(self):
        result = scale_limits([
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 10,
            },
            {
                'tag': 'tag2',
                'period_sec': 1,
                'count': 20,
            },
        ], 0.1)

        self.assertEqual(result, [
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 1,
            },
            {
                'tag': 'tag2',
                'period_sec': 1,
                'count': 2,
            },
        ])

    def test_input_not_changed(self):
        input = [
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 10,
            },
        ]
        scale_limits(input, 0.1)

        self.assertEqual(input, [
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 10,
            },
        ])
