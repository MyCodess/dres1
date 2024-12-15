import sys

# #__  print(dir())
# #--I- __package__ only sichtbar, if you call them as module (py -m a.b.c) and NOT as file (py a/b/c.py)
print("---------- file, package, name, path : ----------\n", __file__, __package__, __name__, __path__, sep="  ::  ")
# #__1ok:  print("- sys-path in :", __name__) ; for ii in range(len(sys.path)): print(sys.path[ii])
print("--- sys.path entries in:  ", __name__, "\n", "\n".join("{}".format(ii) for ii in sys.path), "\n---", sep="")
