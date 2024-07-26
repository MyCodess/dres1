.. |YEAR1| date::  %Y

================================================================================
Docutils Directives by Examples (reST / reStructuredText Directives)
================================================================================

:Author: KouKa
:Version: 0.91
:Date: 2023-07-10
:Copyright: GNU General Public License ver.3, GPL-3.0 , 2014-|YEAR1|

.. contents::
   :backlinks: none

.. section-numbering::

.. header::  Docutils Directives  Examples -header


.. footer::  Docutils Directives  Examples -footer

.. target-notes::

.. note::
   - Compare this page with its `reST source file <./ rst-directives1-Docutils.rst>`_
   - see `Docutils Reference <https://docutils.sourceforge.io/docs/ref/rst/directives.html>`_ for details, specification, description ... ! Here ONLY some examples !


Directives Definition/Notes
------------------------------------------------------------

- Directives are a general-purpose extension mechanism, a way of adding support for new constructs without adding new syntax. 
- Directives-Structure/Syntax/elements/Def::

    ".." <directive type/name> "::" <directive Arguments>
        <directive Options>....
        \n
        <directive body/content>

- short:   ".." <directive type/name> "::" <directive block>

........................................................................

Admonitions
------------------------------------------------------------

- safety messages for notes/warnings/attention/tips/hazard/important/...
- types:  attention, caution , danger, error, hint, important, note, tip, warning

.. warning::
   thunderstorm, heavy snowfall and ice storms !
   icy conditions on the roads !

.. note::
   Don't forget the key!
   check it twice ...!

.. attention::
   heavy traffic at the weekend !
   avoid highways !

........................................................................


Topic
------------------------------------------------------------

A topic is like a block quote with a title, or a self-contained section with no subsections. 

.. topic:: Topic-Title-1

    Subsequent indented lines comprise
    the body of the topic, and are
    interpreted as body elements.

........................................................................


Sidebar
------------------------------------------------------------

Sidebars are like miniature, parallel documents that occur inside other documents, providing related or reference material. 

.. sidebar:: Optional Sidebar Title-1
   :subtitle: Optional Sidebar Subtitle-1

   Subsequent indented lines comprise the body of the sidebar, and are
   interpreted as body elements.

here normal text again after sidebar directive ...

here normal text again after sidebar directive ...

........................................................................

math
------------------------------------------------------------

"math" directive inserts blocks with mathematical content
::

    .. math::

    .. not-working-yet   α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)

........................................................................


epigraph
------------------------------------------------------------

often a quotation or poem, at the beginning of a document or section.

.. epigraph::

   No matter where you go, there you are.

   -- Buckaroo Banzai

........................................................................


highlights
------------------------------------------------------------

Highlights summarize the main points of a document or section, often consisting of a list.

.. highlights::

   - point1
   - point2
   - point3
   - point4

........................................................................


pull-quote
------------------------------------------------------------

A pull-quote is a small selection of text "pulled out and quoted", typically in a larger typeface. Pull-quotes are used to attract attention, especially in long articles.

.. pull-quote::

   That's one small step for a man, a giant leap for mankind.
   Neil Armstrong

normal est further ...

........................................................................


compound
------------------------------------------------------------

.. compound::

   The 'rm' command is very dangerous.  If you are logged
   in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.

........................................................................


Table
------------------------------------------------------------

- table directive: a bit  more than what the reStructuredText inline table syntax supplies (see also csv-table directive).
- DIFF:   :width: option is the table-width as a whole <-->  :widths:  defines each column width !
- the UNIT only in :width:  ,as :width:  30em , or :width:  80% , but NO units any more in :widths: !
- if setting the column widths as percentage, then WITHOUT any % symbol,..., as :widths: 20,50,30
  otherwise also units as em,.., eg:   :widths: 20em,50em,30em , or percentage:   :widths: 20,50,30
  

.. table:: "TITLE-1 of the table directive"
   :width:  60%
   :widths: 50,30,20
   :align: center

   ========= ============= ============
   C1           C2          C3
   ========= ============= ============
   aa1         bb1           cc1
   aa2  xxx    bb2           cc2
   aa3         bb3           cc3
   ========= ============= ============

........................................................................


csv-table
------------------------------------------------------------
- create a table from CSV (comma-separated values) date !
- the csv data may be inline or an external file/URI !
- Within the CSV data/file, you can use RST inline markups !
- delimiter can be defined instead of comma! only a SINGLE character !

.. csv-table:: Title1-of-csv-table-example
   :header: "col1",  "col2", "col3"
   :width:  70%
   :widths:  50, 30, 20
   :align: center
   :delim: :

   aa1:bb1:cc1
   aa2:bb2:cc2
   aa3:bb3:cc3

........................................................................


list-table
------------------------------------------------------------

- "list-table" directive is used to create a table from data in a uniform two-level bullet list.
- "Uniform" means that each sublist (second-level list) must contain the same number of list items.

.. list-table:: Frozen Delights!
   :width: 80%
   :widths: 30, 20,50
   :header-rows: 1
   :align: center

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

........................................................................


replace
------------------------------------------------------------

-  "replace" directive is used to indicate replacement text for a substitution reference.

.. |reST1| replace:: reStructuredText

Yes, |reST1| is a long word, so I can't blame anyone for wanting to abbreviate it to reST !

........................................................................


date
------------------------------------------------------------

- !  This directive may be used in substitution definitions ONLY !
- "date" directive generates the current local date and inserts it into the document as text
- check Python's time.strftime() function for the format !
- The default format is "%Y-%m-%d" (ISO 8601 date), but time fields can also be used. 

.. |date1| date::  %Y-%m-%d
.. |time1| date::  %H:%M
.. |dateTime1| date::  %Y-%m-%d--%H:%M

Today's date is |date1|.

- e.g.:  YYYY-MM-DD  ==   date::  %Y-%m-%d  , output:   |date1|
- e.g.:  YYYY-MM-DD--HH:mm ==   date::    %Y-%m-%d at %H:%M , output:  |dateTime1|

........................................................................


meta
------------------------------------------------------------

- "meta" directive is used to specify metadata to be stored in, e.g., HTML meta elements or as ODT file properties.
- e.g.: writing meta data into html header of the file: (check the HTML source code of this file for meta entries in the <head> section !)

.. meta::
   :description: The reStructuredText directives by example ver. 0.9
   :keywords: reST, reStructuredText, directives, examples 1

