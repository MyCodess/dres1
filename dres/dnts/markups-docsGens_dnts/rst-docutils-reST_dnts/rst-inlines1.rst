.. |YEAR1| date::  %Y

============================================================
Docutils Roles by Examples (reST / reStructuredText Roles)
============================================================

:Author: KouKa
:Revision: 0.91
:Date: 2023-07-10
:Copyright: GNU General Public License ver.3, GPL-3.0 , 2014-|YEAR1|

.. contents::

.. note:: see `Docutils Quick reST <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_ for details, specification, References, ...

literal/code Blocks
----------------------------------------
- ! compare this inline "Literal Blocks" with the directives code:: and parsed-literal:: but also the :code: Role !

normal text / paragraph ...
and ...

here a literal/code Block::

    NO **reST** parsing at all in a literal Block !
    keeping whitespaces     , newlines


    blank lines, **not-bold**,
    *no inline parsing* ...
    up to the intendation back to the normal text !

next normal paragraph
and ....

..............................................................................

Line Blocks
----------------------------------------

normal text / paragraph ...

| preserving **Line breaks and initial indents** , but otherwise **do parsing** for reST tags !
|       Line blocks are useful for addresses,
| verse, and adornment-free lists.
|
| Each new line begins with a
| vertical bar ("|").
|     Line breaks and initial indents
|     are preserved.
| Continuation lines are wrapped
  portions of long lines; they begin
  with spaces in place of vertical bars.

next normal paragraph
and ....

..............................................................................

Block Quotes
----------------------------------------
Block quotes are just
    Just indented paragraphs , but otherwise **do parsing** for reST tags !

        and they may nest.
        and back        and *forth*
        and so on ...
        BUT they are parsed for **reST** tags

        and new lines are NOT preserved! if no blank lines in between, as in reST format ...

next normal paragraph
and ....



