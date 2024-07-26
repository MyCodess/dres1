===================================
reST-Tables-eg1:
===================================

- see:  https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#tables
- see:  https://docutils.sourceforge.io/docs/ref/rst/directives.html#tables

Grid-Table:
----------------------------

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+


Simple-Table:
----------------------------
=====  =====  =======
  A      B    A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======

=====  =====
col 1  col 2
=====  =====
1      Second column of row 1.
2      Second column of row 2.
       Second line of paragraph.
3      - Second column of row 3.

       - Second item in bullet
         list (row 3, column 2).
\      Row 4; column 1 will be empty.
=====  =====

- Simple tables allow multi-line rows (in all but the first column) and
- column spans, but not row spans.
- ("=") is used for top and bottom table borders, and to separate optional header rows from the table body.
- ("-") may optionally be used to explicitly and/or visually separate rows (or for multi column spans).
- The rightmost column is unbounded; text may continue past the edge of the table (as indicated by the table borders). However, it is recommended that borders be made long enough to contain the entire text.


Table-Directive "table":
----------------------------
- width  option: table-width (eg: 100 % / 10 cm / 60 pt) 
- widths option: columns-width

.. table:: Truth table for "not"
   :align:  left
   :width:  100 %
   :widths: 40  80

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====



Table-Directive "List-Tables":
---------------------------------------

- see https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table

.. list-table:: Frozen Delights!
   :widths: 15 10 30
   :header-rows: 1

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


