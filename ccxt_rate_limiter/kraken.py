# public only
def kraken_wrap_defs():
    # https://support.kraken.com/hc/en-us/articles/206548367-What-are-the-API-rate-limits-#1
    return [
        {
            'regex': 'public',
            'tags': ['public'],
            'count': 1,
        },
    ]


# https://support.kraken.com/hc/en-us/articles/206548367-What-are-the-API-rate-limits-#1
def kraken_limits():
    return [
        {
            'tag': 'public',
            'period_sec': 1,
            'count': 1
        },
    ]
