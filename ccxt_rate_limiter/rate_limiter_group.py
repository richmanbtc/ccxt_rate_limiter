import copy
from .rate_limiter import RateLimiter

class RateLimiterGroup:
    def __init__(self, limits=[], wait_sec=0.1):
        self.limits = copy.deepcopy(limits)
        self.limiters = []
        for limit in limits:
            self.limiters.append(RateLimiter(period_sec=limit['period_sec'], count=limit['count'], wait_sec=wait_sec))

    def rate_limit(self, tags=None, count=1):
        for i in range(len(self.limits)):
            if self.limits[i]['tag'] in tags:
                for j in range(count):
                    self.limiters[i].rate_limit()

    def status_info(self):
        result = []
        for i in range(len(self.limits)):
            result.append({
                'tag': self.limits[i]['tag'],
                'recent_count': self.limiters[i].recent_count()
            })
        return result
