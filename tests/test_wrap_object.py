from unittest import TestCase
from ccxt_rate_limiter import wrap_object
from ccxt_rate_limiter.rate_limiter_group import RateLimiterGroup

class Class1:
    def method1(self):
        return 1

    def method2(self):
        return 2

class TestWrapObject(TestCase):
    def test_simple_case(self):
        group = RateLimiterGroup(limits=[
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 1
            }
        ])
        wrap_defs = [
            {
                'regex': 'method1',
                'tags': ['tag1'],
                'count': 1
            }
        ]
        object = Class1()
        wrap_object(object, rate_limiter_group=group, wrap_defs=wrap_defs)

        self.assertEqual(object.method1(), 1)
        self.assertEqual(group.status_info(), [{
            'tag': 'tag1',
            'recent_count': 1,
        }])

    def test_count(self):
        group = RateLimiterGroup(limits=[
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 2
            }
        ])
        wrap_defs = [
            {
                'regex': 'method1',
                'tags': ['tag1'],
                'count': 2
            }
        ]
        object = Class1()
        wrap_object(object, rate_limiter_group=group, wrap_defs=wrap_defs)

        self.assertEqual(object.method1(), 1)
        self.assertEqual(group.status_info(), [{
            'tag': 'tag1',
            'recent_count': 2,
        }])

    def test_not_matched_method(self):
        group = RateLimiterGroup(limits=[
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 1
            }
        ])
        wrap_defs = [
            {
                'regex': 'method1',
                'tags': ['tag1'],
                'count': 1
            }
        ]
        object = Class1()
        wrap_object(object, rate_limiter_group=group, wrap_defs=wrap_defs)

        self.assertEqual(object.method2(), 2)
        self.assertEqual(group.status_info(), [{
            'tag': 'tag1',
            'recent_count': 0,
        }])

    def test_multiple_matched(self):
        group = RateLimiterGroup(limits=[
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 2
            }
        ])
        wrap_defs = [
            {
                'regex': 'method1',
                'tags': ['tag1'],
                'count': 1
            },
            {
                'regex': 'method1',
                'tags': ['tag1'],
                'count': 1
            },
        ]
        object = Class1()
        wrap_object(object, rate_limiter_group=group, wrap_defs=wrap_defs)

        self.assertEqual(object.method1(), 1)
        self.assertEqual(group.status_info(), [{
            'tag': 'tag1',
            'recent_count': 2,
        }])

    def test_substring_matched(self):
        group = RateLimiterGroup(limits=[
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 1
            }
        ])
        wrap_defs = [
            {
                'regex': 'tho',
                'tags': ['tag1'],
                'count': 1
            },
        ]
        object = Class1()
        wrap_object(object, rate_limiter_group=group, wrap_defs=wrap_defs)

        self.assertEqual(object.method1(), 1)
        self.assertEqual(group.status_info(), [{
            'tag': 'tag1',
            'recent_count': 1,
        }])

    def test_other_object_not_changed(self):
        group = RateLimiterGroup(limits=[
            {
                'tag': 'tag1',
                'period_sec': 1,
                'count': 1
            }
        ])
        wrap_defs = [
            {
                'regex': 'method1',
                'tags': ['tag1'],
                'count': 1
            },
        ]
        object = Class1()
        other_object_before = Class1()
        wrap_object(object, rate_limiter_group=group, wrap_defs=wrap_defs)
        other_object_after = Class1()

        self.assertEqual(other_object_before.method1(), 1)
        self.assertEqual(other_object_after.method1(), 1)
        self.assertEqual(group.status_info(), [{
            'tag': 'tag1',
            'recent_count': 0,
        }])

        self.assertEqual(object.method1(), 1)
        self.assertEqual(group.status_info(), [{
            'tag': 'tag1',
            'recent_count': 1,
        }])

