import time
from unittest import TestCase
from ccxt_rate_limiter.rate_limiter_group import RateLimiterGroup

class TestRateLimiterGroup(TestCase):
    def test_rate_limit_matched_tag(self):
        group = RateLimiterGroup(limits=[
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 1
            }
        ])
        group.rate_limit(tags=['tag2'])
        self.assertEqual(group.status_info(), [{
            'tag': 'tag1',
            'recent_count': 0,
        }])

    def test_rate_limit_not_matched_tag(self):
        group = RateLimiterGroup(limits=[
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 1
            }
        ])
        group.rate_limit(tags=['tag2'])
        self.assertEqual(group.status_info(), [{
            'tag': 'tag1',
            'recent_count': 0,
        }])

    def test_rate_limit_multiple_tag(self):
        group = RateLimiterGroup(limits=[
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 1
            },
            {
                'tag': 'tag2',
                'period_sec': 1,
                'count': 1
            }
        ])
        group.rate_limit(tags=['tag1', 'tag2'])
        self.assertEqual(group.status_info(), [{
            'tag': 'tag1',
            'recent_count': 1,
        }, {
            'tag': 'tag2',
            'recent_count': 1,
        }])

    def test_rate_limit_duplicated_tag(self):
        group = RateLimiterGroup(limits=[
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 1
            },
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 1
            },
        ])
        group.rate_limit(tags=['tag1'])
        self.assertEqual(group.status_info(), [{
            'tag': 'tag1',
            'recent_count': 1,
        }, {
            'tag': 'tag1',
            'recent_count': 1,
        }])

    def test_rate_limit_count(self):
        group = RateLimiterGroup(limits=[
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 2
            }
        ])
        group.rate_limit(tags=['tag1'], count=2)
        self.assertEqual(group.status_info(), [{
            'tag': 'tag1',
            'recent_count': 2,
        }])
