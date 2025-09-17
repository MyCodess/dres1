====================================================================
classesTree_diagram-eg1 (inheritance_diagram)
====================================================================

sphinx.ext.inheritance_diagram eg1:
-------------------------------------------------------

- see REF-docs:  usage/extensions/inheritance.html
- sphinx.ext.inheritance_diagram – Include inheritance diagrams !
- For each given class, and each class in each given module, the base classes are determined. Then, from all classes and their base classes, a graph is generated which is then rendered via the graphviz extension to a directed graph.
- ! works for modues/classes but NOT for pkg/DIR as parameter !!

Diagram eg (dummy-test-module):
--------------------------------------------

.. inheritance-diagram::  classDiag1

Diagram eg: logging...
-------------------------------------------

.. inheritance-diagram:: logging

Diagram eg: logging...
-------------------------------------------

.. inheritance-diagram:: logging.handlers

Diagram eg: abc
-------------------------------------------

.. inheritance-diagram:: abc

Diagram eg: collections.abc
--------------------------------------------

.. inheritance-diagram::  collections.abc

- 
