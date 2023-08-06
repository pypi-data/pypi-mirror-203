"""Decorator function zoo.
"""

from inspect import isclass
import logging
from time import perf_counter_ns, sleep, perf_counter
import warnings
import functools
from typing import Mapping
from collections import namedtuple
from datetime import datetime
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

from dataclasses import dataclass, field

try:
    from .misc import setup_logger
except:
    def setup_logger(): pass

__all__ = [
    'record_stats', 'register', 'get_function', 'get_class',
    'preprocess', 'postprocess', 'run_before', 'run_after', 
    'retry', 'thread', 'thread_in_pool', 'timeout',
    'returns', 'yields', 'fix_this',
    'ignores', 'fallsback', 'returns_time', 'logs',
]


@dataclass
class UsageStats:
    num_calls: int = 0
    num_errors: int = 0
    total_time: float = 0
    min_time: float = float('inf')
    max_time: float = 0
    error_types: dict = field(default_factory=dict)
    output_types: dict = field(default_factory=dict)
    
    def update_time(self, duration):
        self.total_time += duration
        self.min_time = min(duration, self.min_time)
        self.max_time = max(duration, self.max_time)
        
    def update_errors(self, error):
        self.num_errors += 1
        self.error_types[type(error)] = self.error_types.get(type(error), 0) + 1
        
    def update_outputs(self, output):
        self.output_types[type(output)] = self.output_types.get(type(output), 0) + 1


def record_stats():
    
    stats = UsageStats()
    
    def decorator(fn):
        
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            
            stats.num_calls += 1
            
            try:
                t_before = perf_counter()
                output = fn(*args, **kwargs)
                stats.update_time(perf_counter() - t_before)
                stats.update_outputs(output)
                return output
            except Exception as e:
                stats.update_errors(e)
                raise
        
        wrapper.stats = stats
        return wrapper
    return decorator


# registry --------------------------------------------------------------------

function_registry = {}
class_registry = {}


def get_function(name):
    return function_registry[name]

def get_class(name):
    return class_registry[name]


def register(name=None):
    def decorator(func_or_class):
        key = name or func_or_class.__name__
        if isclass(func_or_class):
            class_registry[key] = func_or_class
        else:
            function_registry[key] = func_or_class
        return func_or_class
    return decorator

# chain/pipeline --------------------------------------------------------------------

def chain_functions(*funcs):
    def chained(*args, **kwargs):
        output = funcs[0](*args, **kwargs)
        for func in funcs[1:]:
            output = func(output)
        return output
    return chained

def preprocess(pre_func, *more_funcs):
    def decorator(fn):
        return chain_functions(pre_func, *more_funcs, fn)
    return decorator


def postprocess(post_func, *more_funcs):
    def decorator(fn):
        return chain_functions(fn, post_func, *more_funcs)
    return decorator


# sequence --------------------------------------------------------------------


def run_before(pre_func, *more_funcs):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for func in (pre_func, *more_funcs):
                func(*args, **kwargs)
            return fn(*args, **kwargs)
        return wrapper
    return decorator


def run_after(post_func, *more_funcs):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            output = fn(*args, **kwargs)
            for func in (post_func, *more_funcs):
                func(*args, **kwargs)
            return output
        return wrapper
    return decorator


# retry --------------------------------------------------------------------


def retry(n, interval_wait=0, log_level=logging.WARNING):

    def decorator(fn):
        
        ordinal_suffix = {1: 'st', 2: 'nd', 3: 'rd'}
        logger = setup_logger(name=fn.__name__)
        
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for i in range(1, n+1):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    if i < n:
                        logger.log(
                            log_level,
                            f"{e!r} raised in `{fn.__name__}` in {1}{ordinal_suffix.get(i, 'th')} try out of {n}! Retrying after {interval_wait} seconds..."
                        )
                        sleep(interval_wait)
                    else:
                        raise
        return wrapper
    return decorator


retries = retry


# threading --------------------------------------------------------------------


def thread(deamon=None):
    def decorator(fn):
        
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            thread = Thread(target=fn, name=fn.__name__,
                            args=args, kwargs=kwargs, daemon=deamon)
            thread.start()
            return thread
                
        return wrapper
    
    return decorator

    
def thread_in_pool(max_workers=None):
    
    def decorator(fn):
        
        executor = ThreadPoolExecutor(max_workers=max_workers)
        
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            # returns `Future` object
            return executor.submit(fn, *args, **kwargs)
        
        wrapper.executor = executor
        
        return wrapper
    
    return decorator


def timeout(seconds):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            with ThreadPoolExecutor() as executor:
                future = executor.submit(fn, *args, *kwargs)
                return future.result(timeout=seconds)
        return wrapper
    return decorator


# namedtuplify --------------------------------------------------------------------


def returns(*field_names, type_name=None, **name2description):
    def decorator(fn):
        output_type_name = type_name or fn.__name__ + '_output'
        output_field_names = field_names + tuple(name2description.keys())
        FuncOutput = namedtuple(output_type_name, output_field_names)

        doc = fn.__doc__ + '\n' if fn.__doc__ else ''
        doc += 'Returns:\n'
        for name in field_names:
            doc += f'\t{name}\n'
        for name in name2description:
            doc += f'\t{name}: {name2description[name]}\n'
        fn.__doc__ = doc

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            output = fn(*args, **kwargs)
            if isinstance(output, Mapping) and set(output.keys()) == set(field_names):
                return FuncOutput(**output)
            elif isinstance(output, tuple):
                return FuncOutput(*output)
            else:
                return FuncOutput(output)

        return wrapper
    return decorator


def yields(*field_names, type_name=None, **name2description):

    def decorator(fn):
        output_type_name = type_name or fn.__name__ + '_output'
        output_field_names = field_names + tuple(name2description.keys())
        FuncOutput = namedtuple(output_type_name, output_field_names)

        doc = fn.__doc__ + '\n' if fn.__doc__ else ''
        doc += 'Yields:\n'
        for name in field_names:
            doc += f'\t{name}\n'
        for name in name2description:
            doc += f'\t{name}: {name2description[name]}\n'
        fn.__doc__ = doc

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            for item in fn(*args, **kwargs):
                if isinstance(item, Mapping):
                    yield FuncOutput(**item)
                elif isinstance(item, tuple):
                    yield FuncOutput(*item)
                else:
                    yield FuncOutput(item)

        return wrapper
    return decorator


def return_time(milis=False, micros=False, nanos=False):    # defaults to seconds

    def decorator(fn):
        FuncOutput = namedtuple(fn.__name__ + '_output', ('output', 'time'))

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            t_before = perf_counter_ns()
            result = fn(*args, **kwargs)
            duration = perf_counter_ns() - t_before     # nanoseconds
            if milis:
                duration = duration // 1000
            elif micros:
                duration = duration // 1000_000
            elif not nanos: # seconds
                duration = duration / 1000_000_000                

            return FuncOutput(result, duration)

        return wrapper
    return decorator


returns_time = return_time


# logging --------------------------------------------------------------------


def repr_signature(*args, **kwargs):
    args_repr = [repr(a) for a in args]
    kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
    return ', '.join(args_repr + kwargs_repr)


def repr_call(fn, *args, **kwargs):
    return f'{fn.__name__}({repr_signature(*args, **kwargs)})'


# inspired by https://ankitbko.github.io/blog/2021/04/logging-in-python/
def log(logger=None, to_file=None, file_mode='a',
         before=logging.DEBUG, after=logging.DEBUG, exception=logging.ERROR):
    def decorator(fn):
        logger_name = logger if isinstance(logger, str) else fn.__name__
        mylogger = setup_logger(
            base=logger, name=logger_name, log_file=to_file, mode=file_mode)

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            t_before = datetime.now()
            if before:

                signature = repr_signature(*args, **kwargs)
                mylogger.log(
                    before, f"Function `{fn.__name__}` called with args: ({signature})")
            try:
                result = fn(*args, **kwargs)
                t_after = datetime.now()
                if after:
                    mylogger.log(
                        after, f"Function `{fn.__name__}` returned after {str(t_after-t_before)} with output: {result}")
                return result
            except Exception as e:
                t_exception = datetime.now()
                if exception:
                    mylogger.log(
                        exception, f"{e!r} raised in `{fn.__name__}` after {str(t_exception-t_before)}!\n{str(e)}".strip())
                raise e
        return wrapper
    return decorator


logs = log

# warning --------------------------------------------------------------------


def fix_this(msg=None, warn_each_call=True):
    def decorator(fn):
        message = f'You need to fix `{fn.__name__}`! '
        if msg:
            message += msg
        warnings.warn(message=message)

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            if warn_each_call:
                warnings.warn(message=message)
            return fn(*args, **kwargs)

        return wrapper
    return decorator


# exception --------------------------------------------------------------------


def ignore(*exceptions):
    def decorator(fn):

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except Exception as e:
                for ignored_ex in exceptions:
                    if isinstance(e, ignored_ex):
                        break
                else:
                    raise e

        return wrapper
    return decorator


def fallback(exception, fallback):
    def decorator(fn):

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except exception as e:
                if callable(fallback):
                    return fallback(*args, **kwargs)
                else:
                    return fallback

        return wrapper
    return decorator


ignores = ignore
fallsbacks = fallback


if __name__ == '__main__':

    @returns('x', 'y')
    def myfunction(x):
        return x, x+1

    @yields('a', 'b')
    def mygenerator(x):
        for i in range(x):
            yield i, i*2

    @fix_this('It always prints ValueError, errors should be raised!')
    def please(x):
        print('ValueError')

    def log_plus(x):
        return x + 1

    def log_minus(s):
        print

    @preprocess(int)
    @postprocess(str)
    def process(x):
        print(type(x))
        return x * 5


    @retry(3)
    def errorenous(x):
        return x / 0
    
    errorenous(10)