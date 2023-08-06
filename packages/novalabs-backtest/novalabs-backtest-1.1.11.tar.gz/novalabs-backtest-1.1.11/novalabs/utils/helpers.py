from datetime import datetime, timedelta
from typing import Optional, Dict
import time
import re
import traceback


def convert_candle_to_timedelta(candle: str) -> timedelta:
    multi = int(float(re.findall(r'\d+', candle)[0]))
    if 'm' in candle:
        candle_duration = timedelta(minutes=multi)
    elif 'h' in candle:
        candle_duration = timedelta(hours=multi)
    elif 'd' in candle:
        candle_duration = timedelta(days=multi)
    else:
        raise ValueError(f"Please enter a valid candle value. Must contain the letter m, h or d.")

    return candle_duration


def convert_max_holding_to_candle_nb(candle: str, max_holding: timedelta) -> int:
    """
    Return:
        the number maximum of candle we can hold a position
    """

    candle_duration = convert_candle_to_timedelta(candle=candle)

    return int(max_holding.total_seconds() / candle_duration.total_seconds())


def get_timedelta_unit(interval: str) -> timedelta:
    """
    Returns: a tuple that contains the unit and the multiplier needed to extract the data
    """
    multi = int(float(re.findall(r'\d+', interval)[0]))

    if 'm' in interval:
        return timedelta(minutes=multi)
    elif 'h' in interval:
        return timedelta(hours=multi)
    elif 'd' in interval:
        return timedelta(days=multi)


def milliseconds_to_interval(interval_ms: int) -> str:
    if interval_ms < 3600000:
        return str(int(60 / (3600000 / interval_ms))) + 'T'
    elif interval_ms < 86400000:
        return str(int(24 / (86400000 / interval_ms))) + 'H'
    else:
        return str(int(interval_ms / 86400000)) + 'D'


def interval_to_minutes_str(interval: str) -> str:
    """Convert a Binance interval string to milliseconds
    Args:
        interval: interval string, e.g.: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
    Returns:
         int value of interval in milliseconds
         None if interval prefix is not a decimal integer
         None if interval suffix is not one of m, h, d, w
    """
    if 'm' in interval:
        interval += 'in'

    if 'h' in interval:
        interval += 'our'

    if 'd' in interval:
        interval += 'ay'

    if 'w' in interval:
        interval += 'eek'

    return interval


def interval_to_minutes(interval: str) -> Optional[int]:
    """Convert a Binance interval string to milliseconds
    Args:
        interval: interval string, e.g.: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
    Returns:
         int value of interval in milliseconds
         None if interval prefix is not a decimal integer
         None if interval suffix is not one of m, h, d, w
    """
    minutes_per_unit: Dict[str, int] = {
        "m": 1,
        "h": 60,
        "d": 24 * 60,
        "w": 7 * 24 * 60,
    }
    try:
        return int(interval[:-1]) * minutes_per_unit[interval[-1]]
    except (ValueError, KeyError):
        return None


def interval_to_milliseconds(interval: str) -> Optional[int]:
    """Convert a Binance interval string to milliseconds
    Args:
        interval: interval string, e.g.: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
    Returns:
         int value of interval in milliseconds
         None if interval prefix is not a decimal integer
         None if interval suffix is not one of m, h, d, w
    """
    seconds_per_unit: Dict[str, int] = {
        "m": 60,
        "h": 60 * 60,
        "d": 24 * 60 * 60,
        "w": 7 * 24 * 60 * 60,
    }
    try:
        return int(interval[:-1]) * seconds_per_unit[interval[-1]] * 1000
    except (ValueError, KeyError):
        return None


def limit_to_start_date(interval: str, nb_candles: int):
    """
    Note: the number of candle is determine with the "now" timestamp
    Args:
        interval: interval string, e.g.: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
        nb_candles: number of candles needed.
    Returns:
        the start_time timestamp in milliseconds for production data
    """
    number_of_milliseconds = interval_to_milliseconds(interval)
    now_timestamp = int(time.time() * 1000)
    return now_timestamp - (nb_candles + 1) * number_of_milliseconds


def is_opening_candle(interval: str,
                      current_date: datetime):
    multi = int(float(re.findall(r'\d+', interval)[0]))
    unit = interval[-1]

    if multi == 1:
        if unit == 'm':
            return current_date.second == 0
        elif unit == 'h':
            return current_date.minute + current_date.second == 0
        elif unit == 'd':
            return current_date.hour + current_date.minute + current_date.second == 0
    else:
        if unit == 'm':
            return current_date.minute % multi + current_date.second == 0
        elif unit == 'h':
            return current_date.hour % multi + current_date.minute + current_date.second == 0


def compute_time_difference(
        start_time: Optional[int],
        end_time: Optional[int],
        unit: str
) -> Optional[float]:
    """

    Args:
        start_time: start time in timestamp millisecond
        end_time: start time in timestamp millisecond
        unit: can be 'second', 'minute', 'hour', 'day'

    Returns:

    """

    start_time_s = int(start_time / 1000)
    end_time_s = int(end_time / 1000)

    if unit == 'second':
        return end_time_s - start_time_s
    elif unit == 'minute':
        return (end_time_s - start_time_s) / 60
    elif unit == 'hour':
        return (end_time_s - start_time_s) / 3600
    elif unit == 'day':
        return (end_time_s - start_time_s) / (3600 * 24)


def interval_to_oanda_granularity(interval: str):
    _number = interval[:-1]
    _letter = interval[-1].upper()

    return f"{_letter}{_number}" if _letter in ['M', 'H'] else f'{_letter}'


def retry_requests(func,
                   retries=10):
    def retry_wrapper(*args, **kwargs):

        attempts = 0
        while attempts < retries:
            try:
                return func(*args, **kwargs)

            except Exception:
                if attempts == 4:
                    traceback.print_exc()
                    raise ConnectionError(f"requests failed {retries} times")

                time.sleep(5)
                attempts += 1

    return retry_wrapper


def format_precision(value: float, precision: int, tick: float, up: bool = True):
    if precision == 0:
        return int(value)

    residue = round(value, precision) % tick

    if up:
        return round(value + tick - residue, precision)
    else:
        return round(value - residue, precision)
