# not accurate
def okex_wrap_defs():
    # https://github.com/ccxt/ccxt/blob/master/python/ccxt/okex.py#L104
    return [
        {
            'regex': 'Get|Post|Delete',
            'tags': ['all'],
            'count': 1,
        },
        {
            'regex': 'Get.*(Position|Balance)',
            'tags': ['get_position'],
            'count': 1,
        },
        {
            'regex': 'Get.*Order',
            'tags': ['get_order'],
            'count': 1,
        },
        {
            'regex': 'Get.*Fill',
            'tags': ['get_fill'],
            'count': 1,
        },
        {
            'regex': 'Get.*Config',
            'tags': ['get_config'],
            'count': 1,
        },
    ]

# 細かすぎるので、デフォルトよりも短いもので、重要なもののみ
# https://www.okex.com/docs/en/#summary-limit
def okex_limits():
    return [
        {
            'tag': 'all',
            'period_sec': 1,
            'count': 6
        },
        {
            'tag': 'get_position',
            'period_sec': 2,
            'count': 10
        },
        {
            'tag': 'get_order',
            'period_sec': 2,
            'count': 10
        },
        {
            'tag': 'get_fill',
            'period_sec': 2,
            'count': 10
        },
        {
            'tag': 'get_config',
            'period_sec': 2,
            'count': 5
        },
    ]
