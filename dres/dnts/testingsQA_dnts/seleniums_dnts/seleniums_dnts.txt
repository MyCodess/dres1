_____________________ Seleniums_dnts /testingsQA ____________________________________________
/:230400  :  try1


#####  ==========  urls/docs/helps/... :
	- https://www.selenium.dev/
	- https://github.com/SeleniumHQ/seleniumhq.github.io/
	- https://pypi.org/project/selenium/
	- https://www.selenium.dev/selenium/docs/api/py/index.html    ##--apiDocs
	- https://github.com/SeleniumHQ/seleniumhq.github.io/tree/trunk/examples/python
    - ! HTML-OL_pages-for-tryling-selm-py-scripts:  https://the-internet.herokuapp.com/
##________________________________________  ___________________________


#####  ==========  setup/install :
	_______:  Selenium-WebDriver_py setup:
	- pip  install  --user  Selenium   ##-- https://pypi.org/project/selenium/
	_______:  Browser-WebDriver:
	- ! https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/ :
	- usu. istalled with the browser, but check it if there/in-path?? bzw. if manually start-able? :
	eg chromium, just try to start it:   chromedriver  ##-- /usr/bin/chromedriver ,  is in extra/chromium package dabei !
	-- otherwise 4 ways to install Browser-WebDrivers (but do manually-install/dw !):
	- PATH:  DW them and add to path 
	- with  Selenium-webdriver-manager (auto-install):  pip install webdriver-manager    ##-- to manage/install browser-webdrivers ...
	- ... see above link!
##________________________________________  ___________________________


#####  ==========  Py-Seleniums (pythons) :

	- !! examples: https://github.com/SeleniumHQ/seleniumhq.github.io/tree/trunk/examples/python
    - ! HTML-OL_pages-for-tryling-selm-py-scripts:  https://the-internet.herokuapp.com/
	- tree-modules-listing:
		- tree -I "__pyca*|devtools|*.js"  /home/u1/.local/lib/python3.10/site-packages/selenium  ##--with-excluding-files -I
		- tree -P "*.py" /home/u1/.local/lib/python3.10/site-packages/selenium  ##--including-only-py-files! still could exclude  -I "__pyca*|devtools|*.js"  as:
		- tree -P "*.py"   -I "__pyca*|devtools|*.js"   /home/u1/.local/lib/python3.10/site-packages/selenium
##________________________________________  ___________________________


##############################  1coll/... : ######################################################

