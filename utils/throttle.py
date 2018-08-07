from datetime import datetime, timedelta
from functools import wraps
from threading import Timer

import time


class throttle(object):
    """
    Decorator that prevents a function from being called more than once every
    time period.
    To create a function that cannot be called more than once a minute:
        @throttle(minutes=1)
        def my_fun():
            pass
    """
    def __init__(self, seconds=0, minutes=0, hours=0):
        self.throttle_period = timedelta(
            seconds=seconds, minutes=minutes, hours=hours
        )
        self.time_of_last_call = datetime.min

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            now = datetime.now()
            time_since_last_call = now - self.time_of_last_call

            if time_since_last_call > self.throttle_period:
                self.time_of_last_call = now
                return fn(*args, **kwargs)

        return wrapper


def throttle2(mindelta):
    def decorator(fn):
        def throttled(*args, **kwargs):
            def call_it():
                throttled.lastTimeExecuted = time.time()

                fn(*args, **kwargs)

            if hasattr(throttled, "lastTimeExecuted"):

                lasttime = throttled.lastTimeExecuted

            else:  # just execute fction

                try:
                    throttled.t.cancel()
                except(AttributeError):
                    pass
                call_it()
                return throttled

            delta = time.time() - throttled.lastTimeExecuted
            try:
                throttled.t.cancel()
            except(AttributeError):

                pass
            if delta > mindelta:

                call_it()
            else:
                timespot = mindelta - delta
                timespot = timespot
                throttled.t = Timer(timespot, call_it)
                throttled.t.start()

        return throttled

    return decorator