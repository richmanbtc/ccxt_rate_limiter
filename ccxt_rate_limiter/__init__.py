import copy
import re
from .rate_limiter_group import RateLimiterGroup

def wrap_object(object=None, rate_limiter_group=None, wrap_defs=None):
    wrap_defs = copy.deepcopy(wrap_defs)

    methods = dir(object)
    for method in methods:
        matched_defs = _extract_matched_defs(method=method, wrap_defs=wrap_defs)

        if len(matched_defs) == 0:
            continue

        def get_wrapped_method(orig_method=None, matched_defs=None):
            def wrapped_method(*args, **kwargs):
                for matched_def in matched_defs:
                    rate_limiter_group.rate_limit(tags=matched_def['tags'], count=matched_def['count'])
                return orig_method(*args, **kwargs)
            return wrapped_method

        orig_method = getattr(object, method)
        setattr(object, method, get_wrapped_method(orig_method=orig_method, matched_defs=matched_defs))

def scale_limits(limits=None, scale=None):
    limits = copy.deepcopy(limits)
    for limit in limits:
        limit['count'] *= scale
        if limit['count'] < 1:
            limit['period_sec'] /= limit['count']
            limit['count'] = 1
    return limits

def _extract_matched_defs(method=None, wrap_defs=None):
    matched_defs = []
    for wrap_def in wrap_defs:
        regex = re.compile(wrap_def['regex'])
        if regex.search(method):
            matched_defs.append(wrap_def)
    return matched_defs
