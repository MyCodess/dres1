#!/usr/bin/env  python


#####  ==========  
print("\n=========================")
print("----------------- 8- yield-stmt on the right-side-of-assigment-= / send data to generator / simple_coroutine : ---------------------")
# python-course.eu/advanced-python/generators-iterators.php.html :
"""
- .send() method allows to pass value to the generator
- send will assign its argument to the x and THEN AFTER that it returns yield value back:")
- x = yield  :  then x will set to the  "sent" argument value AFTER returning the yield-argument to the caller !
- ! ONLY FIRST (Initial) run MUST be with None so as next(simple_coroutine()) ! the following calls MUST send a value, so be called with an argument!
- After running you have to send None value to begin processing!  Sending anything other will raise TypeError !
- next()-call:  starting-the-first-run/loop ! gores up to the first yield-stmt and WAITS for send()-call, since it is on the right-side-of-= ! ")
- yield-on-right-side-of-assignment will WAIT, till its send-call ist executed !")
"""
def simple_coroutine():
    ##__  print("coroutine has been started!")
    x = 0
    while True:
        print("__PRE-yield: ", x)
        ##--II- "- here the yield-value is NOT asigned to x! yield-value is retunred to the CALLER-of-sned!! the SEND-param-value is assigned to x  and then returns the yield-value back to the caller!!")
        x = yield x+2
        print("--POS-yield: ", x)

nts1="""
"""
cr = simple_coroutine()  ##--II-only-assigning cr as pointer to simple_coroutine ! but still NOT running!
print("--start-runnings and sendings: -------")
print("\n-----first-run-(no-send-arg)-returned:  ", next(cr))    ##--II-starting-the-first-run/loop ! gores up to the first yield-stmt and WAITS for send() !
# -!-2try: print("\n-----first-run-returned:  ", next(cr))       ##-- After running you have to send None value to begin processing!  Sending anything other will raise TypeError !
print("\n-----send returned-10:  ", cr.send(10))
print("\n-----send returned-20:  ", cr.send(20))
##________________________________________  ___________________________




#####  ==========  
print("\n=========================")
# https://python3.info/advanced/generator/send.html :
def run():
    print('Starting worker...')
    while True:
        work = yield
        print(f'Processing {work}')

worker = run()
worker.send(None)
worker.send('job1')
worker.send('job2')
worker.send('job3')
##________________________________________  ___________________________

