from contextlib import contextmanager

@contextmanager
def thisFunc(fname, method):
  print("This is the implicit ENTER block")
  my_file = open(fname, method)

  yield my_file
  
  print("This is the implicit EXIT block")
  my_file.close()


with thisFunc("this_file.txt", "w") as example:
  ######### read write statements #########
  example.write("__line_1-2\n")
  print("I'm in WITH block")
  pass

