================================================
doctest-sphinx-eg1 : 
================================================

nts doctest in sphinx :
------------------------------------------------------------------------------
- here examples for **sphinx.ext.doctest** – Test snippets in the documentation
- doctest in sphinx run before docs generation by calling:    make doctest html
- running doctest routines inside documentaions each time before sphinx-docs-build with:   make doctest html
- the test routines can be grouped/labled and run/setup per group ... ! see arguments of  ``doctest::`` and  ``testcode::`` in REFdocs !
- see sphinx-REFdocs of sphinx.ext.doctest in :  .../usage/extensions/doctest.html

- **prereq** for running test routines:
    - the src-code-modules must be accesible for python interpreter, so:
    - either add the src-code-root  to the sys.path in conf.py
    - /OR import/embed it in  ``testsetup::`` tag !
    - /OR set ``doctest_path`` in this rst file!

Two approaches to run doctests inside docs:
------------------------------------------------------------------------------
There are **two** kinds of **test blocks** which can be included in sphinx-docs/rst-files:
    
    1- ``doctest::`` directive , **doctest-style-blocks** : so, standard *"pydoc doctest"* style, which mimic interactive sessions by interleaving Python code (including the interpreter prompt) and output. usu. testing an external module (extra src-code-ile) whose doctest routines are here in this rst-file !

    2- ``testcode:: + testoutput:: /OR doctest::`` directives, **embedded-testcode-blocks** : sphinx.ext.doctest added style of *"code-output-style"* blocks : consist of an ordinary piece of Python code, and optionally, a piece of output for that code. So, here the src-code can be included directly in the rst-file! To check the output of the ``testcode::`` you can use both  `testoutput:: /OR doctest::``

- both styles-directives CAN be mixed and used for each other (see below examples) !
- both styles can use still ``testsetup:: , testcleanup:: , ...``  
- both require access to the source code, so adapted sys.path in conf.py /OR here in testsetup:: ...
- eg for path entry in conf.py: ``import sys, os ; srcRoot = os.path.abspath('../src/') ; sys.path.append(srcRoot)``


src-code here in rst-file (testcode-style) :
---------------------------------------------

.. testcode::

    def f1(ii: int=0): return 10+ii

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

.. doctest::

    >>> f1()
    10
    >>> f1(4)
    14
    >>> f1(2)
    12

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

.. testoutput::

    >>> f1()
    10
    >>> f1(4)
    15
    >>> f1(2)
    12

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


src-code in extra .py-file/module (doctest-style) :
----------------------------------------------------------

.. testsetup::

   ##-- importing ./src/mod3.py ! ./src/ already added to the sys.path in the conf.py !
   import   mod3

.. doctest::

    just-a-doctest-block-as-in-a-module:
    !! the src-code-root must be added to the sys.path in conf.py /OR here in testsetup::-tag !

    >>> mod3.mod1_f1 ()
    10
    >>> mod3.mod1_f1 (10)
    20
    >>> mod3.mod1_f1 (20)
    30

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

.. testcode::

    print (mod3.mod1_f1 (50))
    print (mod3.mod1_f1 (60))

.. testoutput::

   60
   70

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

should be all OK!

