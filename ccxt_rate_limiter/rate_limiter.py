
import threading
import time

class RateLimiter:
    def __init__(self, period_sec=None, count=None, wait_sec=0.1):
        self.period_sec = period_sec
        self.count = count
        self.rate_limit_history = []
        self.lock = threading.Lock()
        self.wait_sec = wait_sec

    def rate_limit(self):
        while True:
            if self.recent_count() < self.count:
                break
            time.sleep(self.wait_sec)

        with self.lock:
            self.rate_limit_history.append(time.time())

    def recent_count(self):
        self.update_history()
        return len(self.rate_limit_history)

    def update_history(self):
        period_sec = self.period_sec
        now = time.time()

        def is_recent(tm):
            return now - period_sec <= tm

        with self.lock:
            self.rate_limit_history = list(filter(is_recent, self.rate_limit_history))
