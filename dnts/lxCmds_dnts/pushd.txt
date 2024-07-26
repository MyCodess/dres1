_____________ pushd,popd,dirs : _______________________
man bash :GNU bash, version 3.2.25:
	-!!! the first  [-n] parameter is a literaly '-n',
	but the secon one is a number, eg -2 !!
	!see man-page-format to see the bold-printing of the first one!
##________________________________________  ___________________________


#####  ==========  
dirs [-clpv] [+n] [-n]
  Without  options,  displays  the  list  of  currently  remembered directories.  The
  default display is on a single line  with  directory  names  separated  by  spaces.
  Directories  are added to the list with the pushd command; the popd command removes
  entries from the list.
  +n     Displays the nth entry counting from the left of the list shown by dirs when
		 invoked without options, starting with zero.
  -n     Displays  the  nth  entry  counting from the right of the list shown by dirs
		 when invoked without options, starting with zero.
  -c     Clears the directory stack by deleting all of the entries.
  -l     Produces a longer listing; the default listing format uses a tilde to denote
		 the home directory.
  -p     Print the directory stack with one entry per line.
  -v     Print the directory stack with one entry per line, prefixing each entry with
		 its index in the stack.
  The return value is 0 unless an invalid option is supplied or n indexes beyond  the
  end of the directory stack.
##________________________________________  ___________________________


#####  ==========  
pushd [-n] [dir]
pushd [-n] [+n] [-n]
  Adds a directory to the top of the directory stack, or rotates  the  stack,  making
  the  new  top  of  the  stack  the  current  working directory.  With no arguments,
  exchanges the top two directories and returns 0,  unless  the  directory  stack  is
  empty.  Arguments, if supplied, have the following meanings:
  +n     Rotates  the  stack so that the nth directory (counting from the left of the
		 list shown by dirs, starting with zero) is at the top.
  -n     Rotates the stack so that the nth directory (counting from the right of  the
		 list shown by dirs, starting with zero) is at the top.
  '-n'     Suppresses  the  normal  change  of directory when adding directories to the
		 stack, so that only the stack is manipulated.
  dir    Adds dir to the directory stack at the top, making it the new current  work-
		 ing directory.
  If the pushd command is successful, a dirs is performed as well.  If the first form
  is used, pushd returns 0 unless the cd to dir fails.  With the second  form,  pushd
  returns  0 unless the directory stack is empty, a non-existent directory stack ele-
  ment is specified, or the directory change to the specified new  current  directory
  fails.
##________________________________________  ___________________________


#####  ==========  
##________________________________________  ___________________________


#####  ==========  
popd [-n] [+n] [-n]
  Removes  entries  from  the  directory  stack.   With no arguments, removes the top
  directory from the stack, and performs a cd to the new top  directory.   Arguments,
  if supplied, have the following meanings:
  +n     Removes  the  nth  entry  counting  from the left of the list shown by dirs,
		 starting with zero.  For example: ``popd +0'' removes the  first  directory,
		 ``popd +1'' the second.
  -n     Removes  the  nth  entry  counting from the right of the list shown by dirs,
		 starting with zero.  For example: ``popd -0'' removes  the  last  directory,
		 ``popd -1'' the next to last.
  '-n'     Suppresses the normal change of directory when removing directories from the
		 stack, so that only the stack is manipulated.
  If the popd command is successful, a dirs is performed as well, and the return sta-
  tus  is  0.   popd returns false if an invalid option is encountered, the directory
  stack is empty, a non-existent directory stack entry is specified, or the directory
  change fails.
