#!/usr/bin/env  python3

print("============ coroutine-1 : ===============================================")
##https://www.geeksforgeeks.org/coroutine-in-python/
# Execution of Coroutine : The execution of the coroutine is similar to the generator. When we call coroutine nothing happens, it runs only in response to the next() and sends () method. 
def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        if prefix in name:
            print(name)
 
# calling coroutine, nothing will happen
corou = print_name("Dear")
 
# This will start execution of coroutine and
# Prints first line "Searching prefix..."
# and advance execution to the first yield expression
print ("- next starting:")
corou.__next__()  ##--/OR next(corou)
print ("- next was called!")

# sending inputs
corou.send("Dear-0 Atul")
corou.send("Atul")
corou.send("Dear-1 Atul")


print("============ coroutine-2 : ===============================================")
# https://zetcode.com/python/async-await/
import asyncio
import time
import random

async def task1():
    wait = random.randint(0, 3)
    print("task 1  wait == ", wait)
    await asyncio.sleep(wait)
    print("task 1 finished, wait == ", wait)

async def task2():
    wait = random.randint(0, 3)
    print("task 2  wait == ", wait)
    await asyncio.sleep(wait)
    print("task 2 finished, wait == ", wait)

async def task3():
    wait = random.randint(0, 3)
    print("task 3  wait == ", wait)
    await asyncio.sleep(wait)
    print("task 3 finished, wait == ", wait)

async def main():
##__    await asyncio.gather(task1(), task2(), task3())
    for x in range(2):
        await asyncio.gather(task1(), task2(), task3())
        print('----------------------------')

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f'Total time elapsed: {t2-t1:0.2f} seconds')

print()
print("_______________=========================================_______________")

