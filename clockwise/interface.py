import collections
import functools
import time

__all__ = ['timing', 'timing_context']


time_dict = collections.defaultdict(list)


def timing(identifier: str):
    def timer_decorator(f):
        @functools.wraps(f)
        def wrap(*args, **kw):
            if __debug__:  # Only time if not in optimized mode.
                ts = time.time()
                result = f(*args, **kw)
                runtime = time.time() - ts

                global time_dict
                time_dict[identifier].append(runtime)
                return result
            else:
                return f(*args, **kw)

        return wrap
    return timer_decorator


class timing_context:

    def __init__(self, identifier: str):
        self.identifier = identifier
        self.ts = None

    def __enter__(self):
        if __debug__:
            self.ts = time.time()
        return self

    def __exit__(self, type, value, traceback):
        if __debug__:
            dt = time.time() - self.ts
            global time_dict
            time_dict[self.identifier].append(dt)
