# not accurate
def bybit_wrap_defs():
    # https://github.com/ccxt/ccxt/blob/master/python/ccxt/bybit.py#L113

    return [
        {
            'regex': 'Get',
            'tags': ['get'],
            'count': 1,
        },
        {
            'regex': 'Post',
            'tags': ['post'],
            'count': 1,
        },
        {
            'regex': 'Post.*Order',
            'tags': ['order'],
            'count': 1,
        },
        {
            'regex': 'Post.*Order.*All',
            'tags': ['order'],
            'count': 10 - 1,
        },
        {
            'regex': 'Get.*Order',
            'tags': ['get_order'],
            'count': 1,
        },
        {
            'regex': 'Get.*Execution',
            'tags': ['get_execution'],
            'count': 1,
        },
        {
            'regex': '(Leverage|ChangePositionMargin|TradingStop)',
            'tags': ['leverage'],
            'count': 1,
        },
        {
            'regex': 'Get.*(Position|WalletBalance)',
            'tags': ['get_position'],
            'count': 1,
        },
        {
            'regex': 'Get.*Funding',
            'tags': ['get_funding_rate'],
            'count': 1,
        },
        {
            'regex': 'Get.*(WalletFund|WalletWithdraw)',
            'tags': ['get_fund_withdraw'],
            'count': 1,
        },
        {
            'regex': 'Get.*ApiKey',
            'tags': ['get_api_key'],
            'count': 1,
        },
    ]

# https://bybit-exchange.github.io/docs/inverse/#t-perendpoint
def bybit_limits():
    return [
        {
            'tag': 'get',
            'period_sec': 1,
            'count': 50,
        },
        {
            'tag': 'post',
            'period_sec': 1,
            'count': 20,
        },
        {
            'tag': 'order',
            'period_sec': 60,
            'count': 100
        },
        {
            'tag': 'get_order',
            'period_sec': 60,
            'count': 600,
        },
        {
            'tag': 'get_execution',
            'period_sec': 60,
            'count': 120,
        },
        {
            'tag': 'leverage',
            'period_sec': 60,
            'count': 75,
        },
        {
            'tag': 'get_position',
            'period_sec': 60,
            'count': 120,
        },
        {
            'tag': 'get_funding_rate',
            'period_sec': 60,
            'count': 120,
        },
        {
            'tag': 'get_fund_withdraw',
            'period_sec': 60,
            'count': 120,
        },
        {
            'tag': 'get_api_key',
            'period_sec': 60,
            'count': 600,
        },
    ]
