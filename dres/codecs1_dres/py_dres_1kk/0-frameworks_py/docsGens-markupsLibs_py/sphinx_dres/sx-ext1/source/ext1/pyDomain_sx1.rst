====================================================================
Python-Domain-Sphinx-eg1 
====================================================================

----------------------------------------------------------
Py-Domain directives to insert/link the docstrings:
----------------------------------------------------------

- !! the links worked ONLY after adding the py-module with autodoc-extension somewhere here in the rst-files!

- Referencing/link to a func of the modules here defined :py:func:`mod2.f1` and here goes on ...!

- Referencing/link to some module here: :py:mod:`mymod1` even if the module-file is not named so but the module-directive with this name was put there!

- Referencing/link to the docstrings of py-StdLib,
  but not working yet (must include stdLib-Src/Docs-path in conf.py):  :py:func:`os.path.join` or
  included with autodoc as for logging, eg:  :py:func:`logging.getLogger`

- Referencing/link to the docstrings of another Class/func:  :py:func:`mod2.f1`

- Referencing/link to the docstrings of another Class/func:  :py:func:`mod2.f2()` : Since this is also integrated here below by autodoc directives, the link targets here instead the original source!

- Referencing/link to the docstrings of another Class/func:  :py:class:`mod1.C1` and done!

- Referencing/link to some module here: :py:mod:`mod1` even if the module-file is not named so but the module-directive with this name was put there!

- Referencing/link to the docstrings of another Class/func:  :py:func:`mod1.C1.f1()`

- Referencing/link to the docstrings of another Class/func:  :py:func:`mod1.C1.f1()` and done!

- Referencing/link to a py-module:  :py:mod:`mod1` and done!

----------------------------------------------------------
autodoc directives to insert/link the docstrings:
----------------------------------------------------------
- in-place docstring of a class using autoclass of autodoc-ext-directive:

    .. autoclass::  mod1.C1
        :no-index:

- in-place docstring of a function using autoclass of autodoc-ext-directive:

    .. autoclass::  mod2.f2()
        :no-index:


- in-place docstring of a function using autofunction of autodoc-ext-directive:

    .. autofunction::  mod2.f2()
        :no-index:

