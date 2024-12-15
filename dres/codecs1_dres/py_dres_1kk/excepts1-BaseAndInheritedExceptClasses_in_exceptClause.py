#!/usr/bin/env  python3

# ###############################################################################################
def exc_clause_prios_1():
    print("\n============- DEFAULT except + sub-/base-class-excepts ========================-")
    """
        - DEFAULT except clause (so only "except:" WITHOUT Exception-Type) MUST be the LAST !! otherwise ERROR ! :
          The last except clause may omit the exception-name to serve as a wildcard.  Use this with extreme caution!
        - ONLY the FIRST MATCHING except clause will be executed out of many except clauses!!
        - so the DEFAULT except clause (WITHOUT Exception-Type) will be ONLY executed, if NO other one matched, as LAST !!
        - docsRF_3.9:  8.3. Handling Exceptions : A class in an except clause is compatible with an exception if it is the same class or a base class thereof, but NOT the other way around ! so an except clause listing a derived class is not compatible with a base class !
    """
    try:
        raise Exception
    except OSError:
        print ("--sub-exc-class will NOT catch its base one !!--")
    except BaseException:
        print ("--BaseException will cath ALL-exceptions!! so works quasi as Default-except-clause! Base-exc-class will DO catch the derived ones !! --")
    except Exception:
        print ("--Exc-itself will match, but never reached, due to Base clause above !--")
    except:
        print ("--Default-Exc MUST be the very LAST Exc-Clause !! --")
    else:
        print("--else ONLY if NO exception raised !!--")
    finally:
        print("--finally will always be executed !!--")
    print("============================================================")


# ###############################################################################################
def exc_clause_classes_prios_1():
    print("\n==========- exp1:  base/subclass Exception :==========================-")
    """
        - base-/sub-exception-classes-catching of Exceptions !
        - error-messages /-No. query !
        - sys.exc_info = exc_info() : Return current exception information: (type, value, traceback). #-: pydoc sys.exc_info
    """
    import sys
    try:
        print(1)
        raise (Exception("msg11-exc", 12))
    except OSError:  ##--->  is a subclass of the raised Exception ! will NOT catch !
        print ("subclass will NOt catch !", 5)
    except BaseException as ex1:  ##---> is a baseclass of the raised Exception ! will catch !
        print (2)
        print ("baseclass  will  catch !", ex1)
        print ("errMsg: ", ex1.args[0])
        print ("errMsg: ", sys.exc_info()[1].args[0])
        print ("errNo:  ", ex1.args[1])
        print ("errNo:  ", sys.exc_info()[1].args[1])
        print ("----- sys.exc_info entries: -----")
        print ("- sys.exc_info-dict: ", sys.exc_info())
        print ("- sys.exc_info-dict-0: ", sys.exc_info()[0].__dict__)
        print ("- sys.exc_info-dict-1: ", sys.exc_info()[1].__dict__)
    else:
        print (3)
    finally:
        print (4)

# ###############################################################################################
def exc_subclassing_tree_1():
    print("\n==========- exp2:  base/subclass Exception :==========================-")
    class B(Exception): pass
    class C(B): pass
    class D(C): pass
    print ("D --> C --> B --> Exception")
    print("----------")

    """ For example, the following code will print B, C, D in that order: """
    for cls in [B, C, D]:
        try:
            raise cls()
        except D: print("D -- catches ONLY D")
        except C: print("C -- cathces C+D ")
        except B: print("B -- catches all B+C+D ! is baseclass of all !")
        ##__   finally:  print("----- finally-done -------------")
    print("----------")

    """ BUT For example, the following code will print: D, C, B """
    for cls in [D, C, B]:
        try: raise cls()
        except D: print("D")
        except C: print("C")
        except B: print("B")
        ##__   finally:  print("----- finally-done -------------")
    print("----------")

    """ BUT For example, the following code will print always: B """
    for cls in [D, C, B]:
        try: raise cls()
        except B: print("B")
        except C: print("C")
        except D: print("D")
        ##__   finally:  print("----- finally-done -------------")
    print("============================================================")

    print("\n===================Multiple Exceptions in one line : =====")
    print("MUST be parenthesized AND comma separated if multiple exceptions in one clause!! :")
    try:
        raise D
    except (D, C):
        print("--##-exc-D", D)
    print("-"*40 + " __1END__ --------")


# ###############################################################################################
def exc_args_1():
    print("\n=================== args of excepts: ====================")
    print("- *args: are params provided to __init__ of the exception !")
    print("- *args: can be theoritically any number of params ! but args[0] should be message and args[1] error-no !: ") 
    try:
        ##__2try:  raise Exception("msg1", 12, 3, 4, "aa","bb")
        raise ValueError("msg11", 123)
    except ValueError  as  ex1:
        print("ValueError: ", ex1, "--args: ", ex1.args , "--length:  ",  len(ex1.args), "-0: ", ex1.args[0], "-1: ", ex1.args[1])
        ##__2try:  raise Exception("msg1", 12, 3, 4, "aa","bb") from ex1
    except Exception   as  ex1:
        print("exception-raised: ", ex1.__class__, ex1, " -: ", ex1.args , " --length: ",  len(ex1.args), "-0: ", ex1.args[0], "-1: ", ex1.args[1] )
    print("-"*40 + " __1END__ --------")
    

# ###############################################################################################
def exc_catch_1():
    try:
        1/0
    except Exception   as  ex1:
        print("Exception: ", ex1.__class__, ex1, " --args: ", ex1.args , " --length: ",  len(ex1.args), " --exc-dict: ", ex1.__dict__)



# ###############################################################################################
if __name__ == "__main__":
    ##__  exc_clause_prios_1()
    ##__  exc_clause_classes_prios_1()
    ##__  exc_subclassing_tree_1()
    ##__  exc_args_1()
    exc_catch_1()
