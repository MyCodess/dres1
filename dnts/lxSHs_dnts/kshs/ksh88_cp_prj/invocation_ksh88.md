UxExp-4ed-12.15. Korn Shell Invocation Arguments
When the Korn shell is involved, it can take options to control its behavior. See Table 12.16.
Table 12.16. Arguments to ksh Command		 Function
-a
 Automatically exports all variables.
-c cmd
 Executes a command string.
-e
 Exits when a command returns a nonzero status.
-f
 Turns off globbing, the expansion of filename metacharacters.
-h
 Causes commands to be treated as tracked aliases.
-i
 Sets the interactive mode.
-k
 Sets the keyword option. All the key arguments to commands will be made part of the environment.
-m
 Causes commands executed in the background to be run in a separate process group, and will continue to run even if Ctrl-C or logout is attempted. Sends a message that the job has terminated when done.
-n
 Can be used for debugging. Commands are scanned, but not executed. Can be used with .x and .v options.
-o
 Allows options to be set by the names listed in Table 12.15 with the set command.
-p
 Turns on privileged mode. Used for running setuid programs.
-r
 Sets the restricted mode.
-s
 Reads command from stdin, the default.
-t
 Causes the shell to exit after executing the first command found in shell input and the .c option is specified.
-u
 Any reference to an unset variable is considered an error.
-v
 Each line of a script or standard input is printed before any parsing, variable substitution, or other processing is performed. Output is written to standard error. Used for debugging.
-x
 Each line of a script or standard input is printed before it is executed. Filename expansion, variable substitution, and command substitution are shown in the output. All output is prepended with the value of the PS4 prompt, a plus sign followed by a space. Lines are written to standard error.
