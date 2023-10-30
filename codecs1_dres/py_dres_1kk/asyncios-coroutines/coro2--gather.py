'''
    pydocs-var/0Refs_HTMLs_py/library/asyncio-task.html :
    Tasks are used to run coroutines in event loops. If a coroutine awaits on a Future, the Task suspends the execution of the coroutine and waits for the completion of the Future. When the Future is done, the execution of the wrapped coroutine resumes.
    Event loops use cooperative scheduling: an event loop runs one Task at a time. While a Task awaits for the completion of a Future, the event loop runs other Tasks, callbacks, or performs IO operations.
'''
print("============ coroutine-2 : ===============================================")
# https://realpython.com/async-io-python/ :   countasync.py
import asyncio

async def count(id):
    AllRunningTaskNames=""
    print("-in--", id)
    asyncio.current_task().set_name(f"taskN_{id}")
    await asyncio.sleep(id)
    for ii in  asyncio.all_tasks():
        AllRunningTaskNames += " , " + ii.get_name()
    print (f"-AllRunningTaskNames inside {id}  :  {AllRunningTaskNames}")
    ##--2chk-: un-comment this to see the effect of cancel, eg for id>2:    if id > 2 : asyncio.current_task().cancel()
    print("-out-", id)

##--this main-coro is the event-loop and runs all coros with gather() :
async def main_asy1():
    asyncio.current_task().set_name(f"mainTaskN")
    print("main-in--")
    await asyncio.gather(count(2), count(3), count(1))
    print ("---------- gather2: ------------------")
    await asyncio.gather(count(0), count(2), count(1))
    print("main-out-")

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main_asy1())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

exit()

