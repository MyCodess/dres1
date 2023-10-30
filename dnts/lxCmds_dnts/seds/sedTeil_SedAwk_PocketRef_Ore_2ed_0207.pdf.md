-kk: pdftotext -f 12 -l 19  SedAwk_PocketRef_Ore_2ed_0207.pdf  sed_ore.txt
    pagebreaks ==  "^L"
##________________________________________  ___________________________


#####  ==========  
1.4 The sed Editor
The stream editor, sed, is a noninteractive editor. It interprets a script and performs the actions in the
script. sed is stream-oriented because, like many Unix programs, input flows through the program and
is directed to standard output. For example, sort is stream-oriented; vi is not. sed's input typically
comes from a file or pipe, but it can also be directed from the keyboard. Output goes to the screen by
default but can be captured in a file or sent through a pipe instead.
Typical uses of sed include:
·
Editing one or more files automatically
·
Simplifying repetitive edits to multiple files
·
Writing conversion programs
sed operates as follows:
·
Each line of input is copied into a pattern space, an internal buffer where editing operations
are performed.
·
All editing commands in a sed script are applied, in order, to each line of input.
·
Editing commands are applied to all lines (globally) unless line addressing restricts the lines
affected.
·
If a command changes the input, subsequent commands and address tests will be applied
to the current line in the pattern space, not the original input line.
·
The original input file is unchanged because the editing commands modify a copy of each
original input line. The copy is sent to standard output (but can be redirected to a file).
·
sed also maintains the hold space, a separate buffer that can be used to save data for later
retrieval.
1.4.1 Command-Line Syntax
The syntax for invoking sed has two forms:
sed [-n] [-e] ' command' file(s)
sed [-n] -f scriptfile file(s)
12
.
This document was created by an unregistered ChmMagic, please go to http://www.bisenter.com to register it. Thanks
The first form allows you to specify an editing command on the command line, surrounded by single
quotes. The second form allows you to specify a scriptfile, a file containing sed commands. Both forms
may be used together, and they may be used multiple times. If no file(s) is specified, sed reads from
standard input.
The following options are recognized:
-n
Suppress the default output; sed displays only those lines specified with the p command or
with the p flag of the s command.
-e cmd
Next argument is an editing command. Useful if multiple scripts or commands are specified.
-f file
Next argument is a file containing editing commands.
If the first line of the script is #n , sed behaves as if -n had been specified.
1.4.2 Syntax of sed Commands
sed commands have the general form:
[address[,address]][!]command [arguments]
sed copies each line of input into the pattern space. sed instructions consist of addresses and editing
commands. If the address of the command matches the line in the pattern space, then the command
is applied to that line. If a command has no address, then it is applied to each input line. If a command
changes the contents of the pattern space, subsequent commands and addresses will be applied to
the current line in the pattern space, not the original input line.
addresses are described in the next section. commands consist of a single letter or symbol; they are
described later, alphabetically and by group. arguments include the label supplied to b or t, the
filename supplied to r or w, and the substitution flags for s .
1.4.2.1 Pattern addressing
A sed command can specify zero, one, or two addresses. An address can be a line number, the
symbol $ (for last line), or a regular expression enclosed in slashes (/pattern/). Regular expressions
are described in Section 1.3. Additionally, \n can be used to match any newline in the pattern space
(resulting from the N command), but not the newline at the end of the pattern space.
13
.
This document was created by an unregistered ChmMagic, please go to http://www.bisenter.com to register it. Thanks
If the command
Then the command is applied to:
specifies:
No address
One address
Each input line.
Any line matching the address. Some commands accept only one
address: a, i, r, q, and = .
Two comma-separated
First matching line and all succeeding lines up to and including a line
addresses
matching the second address.
An address followed by !
All lines that do not match the address.
1.4.2.2 Examples
Command
Action performed
s/xx/yy/g
Substitute on all lines (all occurrences).
/BSD/d
Delete lines containing BSD.
/^BEGIN/,/^END/p
Print between BEGIN and END, inclusive.
/SAVE/!d
Delete any line that doesn't contain SAVE.
/BEGIN/,/END/!s/xx/yy/g
Substitute on all lines, except between BEGIN and END.
Braces ({ }) are used in sed to nest one address inside another or to apply multiple commands to the
matched same address.
[/pattern/[,/ pattern/]]{
command1
command2
}
The opening curly brace must end its line, and the closing curly brace must be on a line by itself. Be
sure there are no spaces after the braces.
1.4.3 Group Summary of sed Commands
In the lists that follow, the sed commands are grouped by function and are described tersely. Full
descriptions, including syntax and examples, can be found afterward in the Section 1.4.4 section.
1.4.3.1 Basic editing
a\
Append text after a line.
c\
Replace text (usually a text block).
14
.
This document was created by an unregistered ChmMagic, please go to http://www.bisenter.com to register it. Thanks
i\
Insert text before a line.
d
Delete lines.
s
Make substitutions.
y
Translate characters (like Unix tr).
1.4.3.2 Line information
=
Display line number of a line.
l
Display control characters in ASCII.
p
Display the line.
1.4.3.3 Input/output processing
n
Skip current line and go to the next line.
r
Read another file's contents into the output stream.
w
Write input lines to another file.
q
Quit the sed script (no further output).
1.4.3.4 Yanking and putting
h
Copy into hold space; wipe out what's there.
H
Copy into hold space; append to what's there.
g
Get the hold space back; wipe out the destination line.
G
Get the hold space back; append to the pattern space.
x
Exchange contents of the hold and pattern spaces.
1.4.3.5 Branching commands
b
Branch to label or to end of script.
t
Same as b, but branch only after substitution.
:label
Label branched to by t or b.
1.4.3.6 Multiline input processing
N
Read another line of input (creates embedded newline).
15
.
This document was created by an unregistered ChmMagic, please go to http://www.bisenter.com to register it. Thanks
D
Delete up to the embedded newline.
P
Print up to the embedded newline.
1.4.4 Alphabetical Summary of sed Commands
sed
Description
Command
#
#
Begin a comment in a sed script. Valid only as the first character of the first line. (Some
versions allow comments anywhere, but it is better not to rely on this.) If the first line of
the script is #n , sed behaves as if -n had been specified.
:label
:
Label a line in the script for the transfer of control by b or t. label may contain up to
seven characters.
[/pattern/]=
=
Write to standard output the line number of each line addressed by pattern.
[address]a\
text
Append text following each line matched by address. If text goes over more than one
a
line, newlines must be "hidden" by preceding them with a backslash. The text will be
terminated by the first newline that is not hidden in this way. The text is not available in
the pattern space, and subsequent commands cannot be applied to it. The results of
this command are sent to standard output when the list of editing commands is finished,
regardless of what happens to the current line in the pattern space.
[address1[,address2]]b[label]
Unconditionally transfer control to :label elsewhere in script. That is, the command
b
following the label is the next command applied to the current line. If no label is
specified, control falls through to the end of the script, so no more commands are
applied to the current line.
[address1[,address2]]c\
text
c
Replace (change) the lines selected by the address(es) with text. (See a for details on
text.) When a range of lines is specified, all lines are replaced as a group by a single
copy of text. The contents of the pattern space are, in effect, deleted and no subsequent
16
.
This document was created by an unregistered ChmMagic, please go to http://www.bisenter.com to register it. Thanks
editing commands can be applied to the pattern space (or to text).
[address1[,address2]]d
d
Delete the addressed line (or lines) from the pattern space. Thus, the line is not passed
to standard output. A new line of input is read, and editing resumes with the first
command in the script.
[address1[,address2]]D
D
Delete the first part (up to embedded newline) of multi-line pattern space created by N
command and resume editing with first command in script. If this command empties the
pattern space, a new line of input is read, as if the d command had been executed.
[address1[,address2]]g
g
Paste the contents of the hold space (see h and H) back into the pattern space, wiping
out the previous contents of the pattern space.
[address1[,address2]]G
G
Same as g, except that a newline and the hold space are pasted to the end of the
pattern space instead of overwriting it.
[address1[,address2]]h
h
Copy the pattern space into the hold space, a special temporary buffer. The previous
contents of the hold space are obliterated. You can use h to save a line before editing it.
[address1[,address2]]H
H
Append a newline and then the contents of the pattern space to the contents of the hold
space. Even if the hold space is empty, H still appends a newline. H is like an
incremental copy.
[address]i\
i
text
Insert text before each line matched by address. (See a for details on text.)
[address1[,address2]]l
l
List the contents of the pattern space, showing nonprinting characters as ASCII codes.
Long lines are wrapped.
[address1[,address2]]n
n
Read the next line of input into the pattern space. The current line is sent to standard
output, and the next line becomes the current line. Control passes to the command
following n instead of resuming at the top of the script.
17
.
This document was created by an unregistered ChmMagic, please go to http://www.bisenter.com to register it. Thanks
[address1[,address2]]N
N
Append the next input line to contents of the pattern space; the new line is separated
from the previous contents of the pattern space by a newline. (This command is
designed to allow pattern matches across two lines.) By using \n to match the
embedded newline, you can match patterns across multiple lines.
[address1[,address2]]p
p
Print the addressed line(s). Note that this can result in duplicate output unless default
output is suppressed by using #n or the -n command-line option. Typically used before
commands that change flow control (d, n, b), which might prevent the current line from
being output.
[address1[,address2]]P
P
Print first part (up to embedded newline) of multiline pattern space created by N
command. Same as p if N has not been applied to a line.
[address]q
q
Quit when address is encountered. The addressed line is first written to the output (if
default output is not suppressed), along with any text appended to it by previous a or r
commands.
[address]r file
r
Read contents of file and append after the contents of the pattern space. There must be
exactly one space between the r and the filename.
[address1[,address2]]s/pat/repl/[flags]
Substitute repl for pat on each addressed line. If pattern addresses are used, the
pattern // represents the last pattern address specified. Any delimiter may be used. Use
\ within pat or repl to escape the delimiter. The following flags can be specified:
n
Replace nth instance of pat on each addressed line. n is any number in the
s
range 1 to 512; the default is 1.
g
Replace all instances of pat on each addressed line, not just the first
instance.
p
18
.
This document was created by an unregistered ChmMagic, please go to http://www.bisenter.com to register it. Thanks
Print the line if the substitution is successful. If several substitutions are
successful, sed will print multiple copies of the line.
w file
Write the line to file if a replacement was done. A maximum of 10 different
files can be opened.
[address1[,address2]]t [label]
Test if successful substitutions have been made on addressed lines, and if so, branch
t
to the line marked by :label. (See b and :.) If label is not specified, control branches to
the bottom of the script. The t command is like a case statement in the C programming
language or the various shell programming languages. You test each case; when it's
true, you exit the construct.
[address1[,address2]]w file
Append contents of pattern space to file. This action occurs when the command is
w
encountered rather than when the pattern space is output. Exactly one space must
separate the w and the filename. A maximum of 10 different files can be opened in a
script. This command will create the file if it does not exist; if the file exists, its contents
will be overwritten each time the script is executed. Multiple write commands that direct
output to the same file append to the end of the file.
[address1[,address2]]x
x
Exchange the contents of the pattern space with the contents of the hold space.
[address1[,address2]]y/abc/xyz/
y
Translate characters. Change every instance of a to x, b to y, c to z, etc.
19
.
This document was created by an unregistered ChmMagic, please go to http://www.bisenter.com to register it. Thanks
.
1.5 The awk Programming Language
