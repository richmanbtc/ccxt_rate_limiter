add rate limiting to ccxt.

## Features

- Rate limit per endpoint


## Install

```bash
pip install "git+https://github.com/richmanbtc/ccxt_rate_limiter.git@v0.0.1#egg=ccxt_rate_limiter"
```

## Usage

### Create RateLimiterGroup

- RateLimiterGroup handles rate limiting by tags.

```python
from ccxt_rate_limiter import scale_limits
from ccxt_rate_limiter.bybit import bybit_limits
from ccxt_rate_limiter.rate_limiter_group import RateLimiterGroup

limits = bybit_limits()
limits = scale_limits(limits, 0.75) # Multiply the rate limit value by a certain magnification to allow a margin.
rate_limiter_group = RateLimiterGroup(limits=limits)
```

### Wrap ccxt instance methods to call RateLimiterGroup before api call

- RateLimiterGroup can be shared between multiple ccxt instances.
- RateLimiterGroup can be shared between multiple threads (thread-safe).

```python
import ccxt
from ccxt_rate_limiter import wrap_object
from ccxt_rate_limiter.bybit import bybit_wrap_defs

bybit = ccxt.bybit({
    'enableRateLimit': False, # disable built-in rate limiter
})

wrap_object(bybit, rate_limiter_group=rate_limiter_group, wrap_defs=bybit_wrap_defs())
```

### Call api

```python
bybit.publicGetTickers()

# rate limiter status
print(rate_limiter_group.status_info())
```

## How to customize rate limiting

Custom rate limiting settings can be used.

see

- ccxt_rate_limiter/binance.py
- ccxt_rate_limiter/bybit.py
- ccxt_rate_limiter/ftx.py

## Supported exchanges

- binance
- bybit
- ftx

## License

CC0

## Developer

### test

```bash
python3 -m unittest tests/test_*
```
