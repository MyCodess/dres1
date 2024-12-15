class myFileHandler():
    def __init__(self, fname, method):
        print("I'm in contructor")
        self.file_obj = open(fname, method)
    def __enter__(self):
        print("I'm in ENTER block")
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("I'm in EXIT block")
        self.file_obj.close()

with myFileHandler("this_file.txt", "w") as example:
  ######### read write statements #########
  example.write("__line_1\n")
  print("I'm in WITH block")
  pass

