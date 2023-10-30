#!/usr/bin/env  python3  -B
""" files-handling, IOs, ...  """

import io

##--- data1:
l1  = list(range(0,10))
l2  = list(range(10,20))
l1s = [str(x)+"\n" for x in l1]
l2s = [str(x)+"\n" for x in l2]
textfile1 = "./0data1/txt1.txt"
textfileOut1 = "./0data1/out1.txt"
binaryfileOut1 = "./0data1/out1.bin.txt"

def open_chk1():
    print ("\n----- open-readonly textfile chk1 : ----------------------")
    fh1 = open(textfile1, "rt")  ##--I-second-param-default for open is : rt == readonly + textfile !
    print ("- type of open() returned filehandle object here is _io.TextIOxxxx for opened text-file: ", type(fh1))
    fh1.close()

def inMemory_textfile_chk1():
    print ("\n----- in-memory-textstream /StringIO chk1 : --------------")
    fh1 = io.StringIO("A text stream in memory saved, but handeled like a normal file!")
    print ("read 5 chars from in-memory-text-stream: ", fh1.read(5) )
    fh1.close()

def read_textfile_chk1():
    print ("\n----- read() textfile chk1 : ----------------------------")
    fh1 = open(textfile1, "rt")  ##--I-second-param-default for open is : rt == readonly + textfile !
    ##__ !!compare the outputs, if open() as bytestream:  fh1 = open(textfile1, "rb")  ##--I-second-param-default for open is : rt == readonly + textfile !
    ##__  txt1 = fh1.read()  ##--I-without argument reads the whole file! : If the argument is omitted, None, or negative, reads and returns all data until EOF.
    txt1 = fh1.read(25)  ##--read n-bytes, here for text files so: n-chars
    print ("- type of returned read() textfile is: ", type(txt1))
    print (txt1)
    print (fh1.readline())
    print (fh1.readline())
    fh1.close()

def read_binfile_chk1():
    print ("\n----- read() binary-/bytes-file chk1 : ------------------------")
    fh1 = open(textfile1, "rb")  ##--I-second-param-default for open is : rt == readonly + textfile !
    ##__ !!compare the outputs, if open() as textstream:  fh1 = open(textfile1, "rt")  ##--I-second-param-default for open is : rt == readonly + textfile !
    ##__  txt1 = fh1.read()  ##--I-without argument reads the whole file! : If the argument is omitted, None, or negative, reads and returns all data until EOF.
    ##---
    print ("---- read(n) of binary-file: ---")
    txt1 = fh1.read(25)  ##--read n-bytes, here for text files so: n-chars
    print ("- type of returned read() bytefile is: ", type(txt1))
    print ("- bytes-read-output: ", txt1)
    print ("- text-from-bytes: interpreting the bytes again back as text/decode based on system-/default-encoding:")
    print (txt1.decode())
    ##---
    print ("---- readline() of binary-file: ---")
    txt2 = fh1.readline()  ##--read one line
    print ("- type of returned readline() bytefile is: ", type(txt2))
    print ("- bytes-readline-output: ", txt2)
    fh1.close()

def readlines_textfile_chk1():
    print ("\n----- readlines() textfile chk1 : ----------------------------")
    fh2 = open(textfile1)
    txt2 = fh2.readlines()
    print("- type of readlines() returned is: list ! each-line one list-item/entry ! whole-file-lines: ", type(txt2))
    print("- readlines() keeps also the EOLs existing in the input-txt-file in the returned-list! :")
    ##__  for line1 in txt2: print (line1 , end="")
    print (txt2)
    fh2.close()

def withOpen_chk1():
    print ("\n----- <with> chk1: ----------------------------------")
    print("- <with> does NOT need close()! it closes itself at the end of with clause! : -------")
    with open(textfile1) as fh3:
        txt3 = fh3.readlines()
        print ("is closed the opened file inside with-clause?: ", fh3.closed)
        print (txt3[3])
    print ("is closed the opened file after with-clause?: ", fh3.closed)

def write_textfile_chk1():
    print ("\n----- write-/overwrite-open-textfile: ----------------------------------") 
    fh1= open(textfileOut1, "w")   ##--II-output-file will be OVERWRITTEN if exists !!
    print ("- type of open() returned filehandle object here is _io.TextIOxxxx for opened text-file: ", type(fh1))
    print ("- NewLine-char, if wanted, must be added to the string-arguments of writexxx()! it is NOT added automaticallay:")
    fh1.write("aa\nbb\ncc\n-----------\n")
    fh1.writelines(l2s)
    print ("- print() method can be also used to write into a flie, which adds as default NewLine-char to the last string!: ")
    print("print1", "print1", file=fh1)  ##--see pydoc print ! as default adds print() the newline at the end, except if  end=xx was redefined !
    print("print2", "print2", file=fh1)
    print("------- binary-write/decoded: ---------", file=fh1)
    print("------- decode:  code/digit-to-char, so like chr() ! bytes MUST be decoded to write as chars into text-filehandle!: ")
    fh1.write((b"aa\nbb\ncc\n-----------\n").decode())
    print("- check the output-txt-file : ", textfileOut1)
    fh1.close()

def write_binaryfile_chk1():
    print ("\n----- write-/overwrite-open-binaryfile, but here also with text in binary-form: ------") 
    with open(binaryfileOut1, "wb") as fh1:
        fh1.write(b"aa\nbb\ncc\n-----------\n")
        print("------- encode:  char-to-code/digit, so like ord() ! string MUST be encoded to write as bytes into binary-filehandle!: ")
        fh1.write("aa\nbb\ncc\n-----------\n".encode())
    print("- check the output-bin-file : ", binaryfileOut1)

def write_binaryBytes_to_textFile_chk1():
    print ("\n-----  Writing Bytes to a TextFile, with-and-without decoding! pyCookBK_3ed--5.17. : ------") 
    with open(textfileOut1, "wt") as fh1:   ##--II-opened as TEXT-filehandle!
        ##--II-you get exception, if write directly bytes to a text-stream WITHOUT applying decode() on bytes!:  fh1.write(b"aa\nbb\ncc\n-----------\n")
        ##--option-1: decode() on bytes:
        fh1.write((b"--- decoded-bytes-into-string:\naa\nbb\ncc\n-----------\n").decode())
        ##--option-2: accessing the underlying binary-layer of the text-filehandle by using buffer-attribute (see discussion there in  pyCookBK_3ed :5.17 ! :
        fh1.buffer.write(b"---binary-layer-accessed-through buffer attrib of the text-stream:\nxx\nyy\nzz\n")
    import sys
    sys.stdout.write       ( "- stdout is a textstream as default ! so writing text/encoded/string to it !\n")
    sys.stdout.buffer.write(b"- stdout is a textstream as default ! so writing bytes to its buffer-layer !\n")
    print("- check the output-txt-file : ", textfileOut1)

##------- main: --------------------------
open_chk1()
inMemory_textfile_chk1()
read_textfile_chk1()
read_binfile_chk1()
readlines_textfile_chk1()
withOpen_chk1()
write_textfile_chk1()
write_binaryfile_chk1()
write_binaryBytes_to_textFile_chk1()

