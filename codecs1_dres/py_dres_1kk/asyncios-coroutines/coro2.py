#!/usr/bin/env python3
# chained.py  :  https://realpython.com/async-io-python/
# Pay careful attention to the output, where part1() sleeps for a variable amount of time, and part2() begins working with the results as they become available:

import asyncio
import random
import time

async def part1(n: int) -> str:
    i = random.randint(0, 3)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result({n})-1"
    print(f"part1({n})-return == {result}.")
    return result

async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 3)
    print(f"part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result({n})-2 derived from {arg}"
    print(f"part2{n, arg}-return == {result}.")
    return result

async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"-->Chained result({n}) => {p2} (took {end:0.2f} seconds).")

async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))

if __name__ == "__main__":
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"___________Program finished in {end:0.2f} seconds._________")


###########################################################################
print("=========================================================================================")
print ("by simply calling a coroutine it will NOT be executed ! it must be awaited to run !! see:")
import asyncio

async def nested():
    return 42

async def main():
    # Let's do it differently now and await it:
    print(await nested())  # will print "42".
    # Nothing happens if we just call "nested()". A coroutine object is created but not awaited, so it *won't run at all*.
    nested()  ##--> generate only RuntimeWarning, BUT does NOT return the 42 as return-value !!

asyncio.run(main())

