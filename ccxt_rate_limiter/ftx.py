# https://github.com/ccxt/ccxt/blob/master/python/ccxt/ftx.py#L106
def ftx_wrap_defs():
    return [
        {
            'regex': 'Get|Post|Delete',
            'tags': ['all'],
            'count': 1,
        },
        {
            'regex': 'Post.*Order',
            'tags': ['send_order'],
            'count': 1,
        },
    ]

# https://docs.ftx.com/#rest-api
# https://help.ftx.com/hc/en-us/articles/360052595091-Ratelimits-on-FTX
def ftx_limits():
    return [
        {
            'tag': 'all',
            'period_sec': 1,
            'count': 30
        },
        {
            'tag': 'send_order',
            'period_sec': 0.2,
            'count': 2, # (Do not send more than 2 orders total per 200ms)
        },
    ]
