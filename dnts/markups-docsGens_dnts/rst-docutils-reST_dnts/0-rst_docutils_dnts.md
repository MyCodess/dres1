=====================================================================
Docutils itself (DocUtils tools) notes
=====================================================================

#####  ==========  docs/refs/notes:

	_______:  Refs/URLs :
    -  **https://docutils.sourceforge.io/rst.html**
    -  https://en.wikipedia.org/wiki/ReStructuredText
    -  https://docutils.sourceforge.io/docs/user/rst/quickref.html
    - !! compare its docs <--> their rst-files !! either click on "view source" /OR DW build-snapshot and check trunk/docutils/docs/ref/rst/ !

	_______:  pythons:
    - **[an example of a Python module fully documented using reStructuredText](https://docutils.sourceforge.io/docutils/statemachine.py)**
##________________________________________  ___________________________


#####  ==========  cmds:

    - for ii in *.rst; do rst2html  $ii   ${ii}.html ; done
    - rst2html   t1.rst   t1.rst.html
    -! pacman -Sy  python-docutils
    - /usr/bin/rst2XXX  as /usr/bin/rst2html , /usr/bin/rst2odt , ... : all belong to python-docutils package !
    -- /OR calling docutils directly  (-h for more):
    - docutils  restTxt1-wipe.rst  restTxt1-wipe.rst.html
    - docutils  restTxt2-qref.rst   restTxt2-qref.rst.html
##________________________________________  ___________________________

#####  ==========  sourcePkg of Docutils:
    - DW: goto "Download" bzw. Snapshots  https://docutils.sourceforge.io/ and DW the "trunk directory" -->  "Download Snapshot" ! 
    - there the rst files are NOT .rst but .txt ! REFs in: trunk/docutils/docs/ref/rst/
    - Generate the HTM-docs of .rst/.txt files:  cd trunk/docutils/ ;  vi  +/"Converting the documentation"  README.txt  ##--So:  cd trunk/docutils ; python  ./tools/buildhtml.py
##________________________________________  ___________________________


#####  ==========  HTML-outputs:
    _______:  CSS customizing (HTML-Design-output-adaptions):
    - customization/adaptions see:  https://docutils.sourceforge.io/docs/howto/html-stylesheets.html
    - the default CSS for HTML-outputs : docutils/writers/html4css1/html4css1.css  (in source-pkg of docutils)
    - adaptions:  rst2html  --stylesheet-path <my-CSS-path> ...
    - to ONLY adapt a few things, put BOTH docutils-default stylesheet and your stylesheet as params, eg:
      rst2html  --stylesheet=html4css1.css,myCss1.css
      Alternatively, copy the default style sheet to the same place as your output HTML files will go and ....
##________________________________________  ___________________________


#####  ==========  conf:
    - see https://docutils.sourceforge.io/docs/user/config.html  !!
    - Configuration files are used for persistent customization (otherwise use cmdline params ...!)
    - ! USER-conf > prj-conf > OS-conf !
    - System/OS-conf:  /etc/docutils.conf  (if any there!)
    - cu-/prj-conf:  ./docutils.conf: This is a project-specific configuration file, located in the current directory, where you CALL docutils-cmds (note that this may have nothing to do with the location of the source files) ! this overrides settings in OS-conf !
    - USER-conf :  ~/.docutils  ; Settings in this file will override corresponding settings in both the system-wide and project-specific configuration files !
    - otherwise use :  --config  cmdline-param  /OR  DOCUTILSCONFIG envVar !
##________________________________________  ___________________________

