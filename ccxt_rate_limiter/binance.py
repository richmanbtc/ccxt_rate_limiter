# not accurate
def binance_wrap_defs():
    # https://github.com/ccxt/ccxt/blob/master/python/ccxt/binance.py#L141
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

# https://www.binance.com/en-NG/support/articles/360004492232
def binance_limits():
    return [
        {
            'tag': 'all',
            'period_sec': 60,
            'count': 1200
        },
        {
            'tag': 'send_order',
            'period_sec': 10,
            'count': 50
        },
        {
            'tag': 'send_order',
            'period_sec': 24 * 60 * 60,
            'count': 160000
        },
    ]
