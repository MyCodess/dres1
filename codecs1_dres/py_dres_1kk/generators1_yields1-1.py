
print("\n============ Generator calls : ===============================================\n")
##--------------- generator : is a method containing yield !
##--------------- generator1-definition:
def f1(nn):
    for ii in range(nn):
        yield ii + 10
        print (f"__ pos-yield, ii == {ii} ")
nts1="""--- generator : is a method containing yield ! to call the gen:
        1- manully: you have to manage it by calling next() AND stop it /check StopIteration-Exc !
        2- in-a-loop bzw. yield-from-stmt : the loop manages next()/StopIterationExc ! """
print (nts1)

print()
print("---------------- 1- manually next() on the iterator pointing to the generator : ----------------")
##--i-    manually calling next() on the iterator pointing to the generator, no-for-/loop-iterator! have to manually manage the END / StopIteration excep : -------
gen1= f1(3)
print (next(gen1), end=" , ")
print (next(gen1), end=" , ")
print (next(gen1), " : calling one more time of next() will cause StopIteration exception !")
##__   print (next(gen1))  ##--this will cause StopIteration exception !!
##__ pause:   input('___ pause! <enter>-to-go-on!')

print()
print("---------------- 2- manually calling next() directly on the Generator : -------------------------")
##--i- manually calling next() directly on the Generator. Each call re-start/re-initialize the generator again, so always the same element returned!:")
print ("__ but make no sense, then each time a NEW generator will be initialized!:")
print(next(f1(3)), end=" , ")
print(next(f1(3)), end=" , ")
print(next(f1(3)), end=" , ")
print()

print()
print("----------------- 3- loop iterates over the gen, after it is initialized with a parameter : ------------")
gen2= f1(3)
for x in gen2:
    print(x, end=" , ")

print()
print("----------------- 3b- loop iterates over the gen,  initialized  directly in the loop : ----------------")
##--i-  calling the iterator on the generator, once initialized with a parameter directly in the loop, without using extra iterator-pointer! so the same as with!:------")
for x in f1(3):
    print(x, end=" , ")

print()
print("---------------- 4- comprenhsion-generator + loop-call over it : -------------------------------------")
g1 = (x for x in range(0,3))
for ii in g1: print (ii, end=" , ")
print()
print ("__ /OR: comprenhsion-gen as one-liner :")
for ii in  (x for x in range(0,3)): print ("__", ii, end=" , ")
print()

print()
print("----------------- 5- yield-from stmts = : ---------------------------------------------")
##--------------- generator-definition:
def f2(nn): yield from range(nn)   ##--II-same as the loop:  for ii in range(nn): yield nn
gen4 = f2(3)
for ii in gen4: print(ii, end=" , ")
print()
##__ print (next(gen4))

print()
print("_______________________________________________________________________")
print("----------------- 8- yield-stmt on the right-side-of-assigment-= / send data to generator / simple_coroutine : ---------------------")
# python-course.eu/advanced-python/generators-iterators.php.html :
def simple_coroutine():
    ##__  print("coroutine has been started!")
    x = 5
    while True:
        print("__ coroutine-PRE-yield: ", x)
        ##--II- "- here the yield-value is NOT asigned to x! yield-value is retunred to the CALLER-of-sned!! the SEND-param-value is assigned to x  and then returns the yield-value back to the caller!!")
        x = yield x+2
        print("__ coroutine-POS-yield: ", x)

cr = simple_coroutine()  ##--II-only-assigning cr as pointer to simple_coroutine ! but still NOT running!
print ("_ next()-call:  starting-the-first-run/loop ! gores up to the first yield-stmt and WAITS for send()-call, dince it is on the right-side-of-= ! ")
next(cr)  ##--II-starting-the-first-run/loop ! gores up to the first yield-stmt and WAITS for send() !
print ("- yield-on-right-side-of-assignment will WAIT, till its send-call ist executed !")
print ("- send will assign its argument to the x and THEN AFTER taht it returne yield value back:")
print("_ send returned: ", cr.send(10))
print("_ send returned: ", cr.send(20))

print()
print("_______________=========================================_______________")

