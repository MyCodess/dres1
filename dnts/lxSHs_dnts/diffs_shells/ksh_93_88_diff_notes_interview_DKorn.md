
	_______:  from: http://slashdot.org/articles/01/02/06/2030205.shtml
	 David Korn Tells All:
David Korn:  First of all, when I talk about ksh here, I am referring to ksh93 which was first released over six years ago. Most UNIX systems ship with ksh88 and most Linux systems ship with pdksh, neither of which has the functionality of ksh93.
There are two different areas of functionality in shells. First is interactive use and the second is scripting. Much of the debate about shells has focused on interactive use only. For example, tcsh is an acceptable shell for interactive use but practically unusable for scripting.
In many cases the argument over which shell is best for interactive use is based upon which key to press for completion. This is a little like arguing that Solaris is better than Windows because of location of the Control and Shift keys or that vi is better than emacs because you you can save a keystroke or two. Most popular shells have similar functionality with respect to interactive use.
It is hard to argue that ksh is any better for interaction, given all the features in tcsh and zsh. But the scripting features in ksh93 are far more advanced than any other shell that I am aware of. For scripting, I feel that ksh is more in the category of perl/tcl/python and I would like to see debates/comparisons for those languages rather than the antiquated bash/csh/etc.
I have not looked at bash for several years and some of the features I describe here might now be implemented by bash. I sent Chet Ramey, author of bash, the list of new features in ksh93 years ago so that if these features get implemented in bash, they would be compatible. Here is a partial list of ksh93 features:
   1. Associative arrays - ksh88 already supports indexed arrays.
   2. Floating point arithmetic + math library functions.
   3. Arithmetic for command similar to C and awk.
   4. Complete ANSI C printf formatting with extensions.
   5. Run time linking of libraries and builtins.
   6. A number of additional substring operations such as offset length.
   7. Full extended regular expression matching capabilities
   8. Compound variables which can be used to represent data aggregates.
   9. Name references for passing aggregate variables by name.
  10. Active variables. Users can trap variable assignment and references by associating intercept functions of the form name.get and name.set.
  11. Ability to make socket connections to servers by name.
  12. read with timeouts.
  13. Conformance to POSIX 1003.2.
  14. Command completion and variable completion, ksh93 only had file name completion.
  15. A key binding mechanism that allows users to bind keys to new editing functions.
Note that only the last two features relate to interactive use. The primary focus of ksh93 is scripting and in this arena it certainly outshines bash. ksh93 runs builtin shell commands much faster than bash.
There is actually a third area of shell functionality which is related to extensibility. In this area ksh93 should be compared to tcl. ksh93 is implemented as a reusable library with a C language API for adding builtins and accessing shell internals. It can be embedded in other programs. For example, dtksh, which is part of the Common Desktop Environment (CDE), uses ksh93 as a library. Similarly, tksh, (written by Jeff Korn) which uses the tk library for graphics, uses ksh93 as a library.
The primary drawback to ksh has been that it was proprietary. This has recently changed however. The new AT&T open source license allows ksh source and binaries to be shipped as part of the system and is now just beginning to start showing up in Linux systems; for example the latest slackware. The source or binary for over a dozen architectures can be downloaded from (http://www.research.att.com/sw/download). Hopefully other systems will start shipping ksh93 and start using this for /bin/sh as well.
