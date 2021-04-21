from ccxt_rate_limiter import _extract_matched_defs
from collections import defaultdict

def test_wrap_defs(limits=None, wrap_defs=None, test_case=None, cases=None):
    # test tag match
    limit_tags = set(map(lambda x: x['tag'], limits))
    wrap_def_tags = set(sum(map(lambda x: x['tags'], wrap_defs), []))
    test_case.assertEqual(limit_tags, wrap_def_tags)

    # test rate_limit
    for case in cases:
        for method in case['methods']:
            matched_defs = _extract_matched_defs(method=method, wrap_defs=wrap_defs)
            tag_counts = defaultdict(int)
            for matched_def in matched_defs:
                for tag in matched_def['tags']:
                    tag_counts[tag] += matched_def['count']
            test_case.assertEqual(tag_counts, case['tag_counts'])
