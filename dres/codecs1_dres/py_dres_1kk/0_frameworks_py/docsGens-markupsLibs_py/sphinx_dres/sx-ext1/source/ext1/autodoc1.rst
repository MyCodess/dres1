====================================================================
autodoc-eg1 (own-module)
====================================================================

nts sphinx.ext.autodoc
-------------------------------------------------

- see REF-docs:  usage/extensions/autodoc.html
- autodoc Includes documentation from docstrings of py-modules directly into sphinx-docs
- modules docstring must be then in correct RST syntax !!
- the modules MUST be importable/findabe for sphinx ! so if needed add your src-code-path-roots to the sys.path in sphinx conf.sys !
- autodoc imports the modules to be documented. If any modules have side effects on import, these will be executed by autodoc when sphinx-build is run.
- For this to work, the docstrings must of course be written in correct reStructuredText. You can then use all of the usual Sphinx markup in the docstrings, and it will end up correctly in the documentation.
- here very simple-basic example, just to include autodoc ! for details check just the above REF-docs ! 
- The example module also contains a ``doctest`` reST-section.
  call ``make doctest html`` to run the tests before generating the project docs !

.. note::
    - ``automodule:: ... ; :members:``  will document all module/pkg members (RECURSIVELY)! so the wohle pkg-tree !
    - By default, autodoc will not generate document for the members that are private, not having docstrings, inherited from super class, or special members.
    - The above can be changed by options:  :undoc-members: , :private-members: , ... !

autodoc of own module : mod1
-------------------------------------------------

.. automodule::  mod1
    :members:

autodoc of own module : mod2
-------------------------------------------------

.. automodule::  mod2
   :members:

