
print("\n============ Generator calls : ===============================================\n")
##--------------- generator : is a method containing yield !
nts1="""
https://python3.info/advanced/index.html#generators
https://python3.info/advanced/generator/yield.html
--- generator : is a method containing yield ! to call the gen:
- ! Python does NOT execute code after calling the generator! Calling a generator will return a generator object.  This object is an iterator
- erst nach dem next(gen1) /loop gen1 /tuple(gen1),list(gen1) / .... its code lines will be really executed!
so to execute its code:
1- manully: you have to manage it by calling next() AND stop it /check StopIteration-Exc !
2- in-a-loop bzw. yield-from-stmt : the loop manages next()/StopIterationExc !
- After last yield raises StopIteration
- There can be one or many yield keywords in a generator function!  Each yield keyword pauses the function and returns the value.
"""
# __ print (nts1)

##--------------- generator1-definition: ----------------------------
def f1(nn):
    for ii in range(nn):
        print (f"-- pre-yield, ii == {ii} ")
        yield ii + 10
        print (f"__ pos-yield, ii == {ii} ")

print()
print("---------------- 1- manually next() on the iterator pointing to the generator : ----------------")
##--i-    manually calling next() on the iterator pointing to the generator, no-for-/loop-iterator! have to manually manage the END / StopIteration excep : -------
gen1= f1(3)
print (next(gen1), end=" , "); print("... do something here ...")
print (next(gen1), end=" , "); print("... do something here ...")
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
print("---------------- 4- Generator Comprehension  + loop-call over it : -------------------------------------")
# -generator comprehension syntax:  (...)   (instead [...] in list-comprehension) !so, it is like a list comprehension but with parentheses instead of (square) brackets!
# -generator comprehension returns a generator (instead of a list in list-compr.) ! so you can use next() or iterate on it whereby keeping the latest status!
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

print("----------------- 6- list(gen1) /tuple/...  will evaluate generator instantly: --------")
# - Instant Evaluation: Using list() will evaluate generator instantly!
# - Functions (list, tuple, set, dict, sum, min, max, all, any, etc) will evaluate generator instantly
# - they iterate also like a loop! so they catch the Exception/StopIteration !
print(tuple( f2(3)))
print(list( f2(3)))
print("_______________________________________________________________________")


print()
print("----------------- 7- several yields in one generator: ---------------------------------")
def run():
    print('one',  end=" :: ")
    print('two',  end=" :: ")
    yield 1
    print('three',  end=" :: ")
    print('four',  end=" :: ")
    yield 2
    print('five')

gen1 = run()
for ii in gen1: print(ii, end=" :: "); print("...")
print("_______________________________________________________________________")

print()
print("----------------- 8- zip + yield: -----------------------------------------------------")
# - https://python3.info/advanced/generator/yield.html
def firstnames():
    yield 'Mark'
    yield 'Melissa'
    yield 'Rick'


def lastnames():
    yield 'Watney'
    yield 'Lewis'
    yield 'Martinez'

for fname, lname in zip(firstnames(), lastnames()):
    print(f'{fname=}, {lname=}')

print("_______________________________________________________________________")


