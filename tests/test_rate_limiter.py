import time
from unittest import TestCase
from ccxt_rate_limiter.rate_limiter import RateLimiter

class TestRateLimiter(TestCase):
    def test_rate_limit(self):
        rate_limiter = RateLimiter(period_sec=1, count=3)

        time1 = time.time()
        rate_limiter.rate_limit()
        rate_limiter.rate_limit()
        rate_limiter.rate_limit()
        time2 = time.time()
        rate_limiter.rate_limit()
        time3 = time.time()

        self.assertLess(time2 - time1, 0.1)
        self.assertGreater(time3 - time1, 0.9)

    def test_recent_count(self):
        rate_limiter = RateLimiter(period_sec=1, count=3)

        self.assertEqual(rate_limiter.recent_count(), 0)

        rate_limiter.rate_limit()
        self.assertEqual(rate_limiter.recent_count(), 1)

        time.sleep(0.5)
        rate_limiter.rate_limit()
        self.assertEqual(rate_limiter.recent_count(), 2)

        time.sleep(0.6)
        self.assertEqual(rate_limiter.recent_count(), 1)

        time.sleep(0.6)
        self.assertEqual(rate_limiter.recent_count(), 0)
