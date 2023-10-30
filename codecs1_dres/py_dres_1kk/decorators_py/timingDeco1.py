#!/usr/bin/env   python
##-- see : https://realpython.com/primer-on-python-decorators/#a-few-real-world-examples

#################### with Arguments of org-func : ################################################
print ("\n=========== Timing-Decorator: ============================================")
print ("- measuring the execution time of a func retuning its return value : -----")
import functools
import time

def timer(func):
    """-- Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"--- Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    sum1 = 0
    for _ in range(num_times):
        sum1 += sum([i**2 for i in range(1000)])
    return sum1

print("- sum value:  ", waste_some_time(3))
print("- sum value:  ", waste_some_time(10))
print()
