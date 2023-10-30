_______________________ diango_dnts ... ________________________________________



#####  ==========  cmds-/....-dj:
    - shell-dj-call  :  (cd in prj1 and):   $ python manage.py shell
##________________________________________  ___________________________

#####  ==========  pydoc-dj for django-api:
    - OL-api-dj:  https://docs.djangoproject.com/en/4.2/py-modindex/

	_______:  pydoc-dj NOT-working without a dj-prj! so:
    - !!  NOT working pydoc django.* as default, because it requires a (dummy-)django-project + django.setup() to be called ... , so:
	some of them (due to their imports in __init__.py) require call of django.setup() and this require s settings.py module, so:
	- must invoke with a dummy-dj-prj-settings (see dj-dnts/-dres for pydoc-dj.py bzw. pydoc-dj.py ) /OR
    -!? if the following ways work for all django classes !?!? try!?

    1-/either:
    go to any django-project-dir containing:  ./manage.py + <prj1>/settings.py ##--here prj1:  my_tennis_club in /up1/mnt/VARUfs/varu/varau/wks/django2/myworld/my_tennis_club/
    export  DJANGO_SETTINGS_MODULE="my_tennis_club.settings"   ##--in: /up1/mnt/VARUfs/varu/varau/wks/django2/myworld/my_tennis_club/my_tennis_club/settings.py
    python  -c "import django, pydoc ; django.setup() ; pydoc.cli()"   django.db.models.Model
    -- bzw. :
	export dummyDjangoPrj_FP=xxxx  PYTHONPATH="${dummyDjangoPrj_FP}:${PYTHONPATH}"  DJANGO_SETTINGS_MODULE="${dummyDjangoPrj_FP}.settings" ;
    python  -c "import django, pydoc ; django.setup() ; pydoc.cli()"  $@ ;
    eg:
    cd <dj-prj1-FP>  ; ##--here: ./my_tennis_club/ prj-DIR containing also my_tennis_club/settings.py : /up1/mnt/VARUfs/varu/varau/wks/django2/myworld/my_tennis_club
    export  DJANGO_SETTINGS_MODULE=my_tennis_club.settings ;  ##-fo setting-file:  /up1/mnt/VARUfs/varu/varau/wks/django2/myworld/my_tennis_club/my_tennis_club/settings.py
    python  -c "import django, pydoc ; django.setup() ; pydoc.    cli()"    django.conf
	
    2-/OR easier, with the default-dj-settings:
	alias pydoc-dj='DJANGO_SETTINGS_MODULE=django.conf.global_settings  python  -c "import django, pydoc ; django.setup() ; pydoc.cli()"' ; eg  pydoc-dj  django.conf
	
    - see also in dj-dnts   pydoc-dj.py bzw. pydoc-dj.sh
    - https://code.djangoproject.com/ticket/31744
##________________________________________  ___________________________

#####  ==========  settings/configs-dj :
    - Ref:  https://docs.djangoproject.com/en/4.2/ref/settings/
    - pydoc_dj.sh   django.conf  /  django.conf.settings
    - dafault dj-app-settings:   pydoc django.conf.global_settings  #bzw.   django/conf/global_settings.py  
    - which apps are surrently installed/active?:  from django.conf import settings ;  settings.INSTALLED_APPS ;
    https://docs.djangoproject.com/en/4.1/topics/settings/  :descp
    https://docs.djangoproject.com/en/4.1/ref/settings/     :Ref
##________________________________________  ___________________________

#####  ==========  TestingsQA-dj:
    --- REFs...:
    - ! Ref-api:  https://docs.djangoproject.com/en/4.2/topics/testing/
    - ! Ref-Tut:  https://docs.djangoproject.com/en/4.2/intro/tutorial05/
    - ! Ref-sj-test-classes-tree-descp:   https://docs.djangoproject.com/en/4.2/topics/testing/tools/#provided-test-case-classes
    - ! https://realpython.com/python-testing/#how-to-use-the-django-test-runner

    --- nts:
    - Ref:  py-unittest based is all dj-functional-testing, see  django.test.TestCase which is a subclass of unittest.TestCase  that runs each test inside a transaction to provide isolation: ...: https://docs.djangoproject.com/en/4.2/topics/testing/overview/
    - OL-api : https://docs.djangoproject.com/en/4.2/py-modindex/ , https://docs.djangoproject.com/en/4.2/topics/testing/overview/  /OR:
    - pydoc  django.test   :  [u1@2209arx my_tennis_club]$   DJANGO_SETTINGS_MODULE="my_tennis_club.settings" ;  python  -c "import django, pydoc ; django.setup() ; pydoc.cli()"  django.test
    - test-client of dj:  django.test.Client , https://docs.djangoproject.com/en/4.2/topics/testing/tools/#django.test.Client

    --- django.test.* /.TestCase  (unittest.TestCase based all):
    - ! tree :  https://docs.djangoproject.com/en/4.2/topics/testing/tools/#provided-test-case-classes :
        py-stdLib--unittest.TestCase  <-- dj SimpleTestCase <-- dj TransactionTestCase <-- dj TestCase + dj LiveServerTestCase
    - ! create your test classes as subclasses of django.test.TestCase rather than unittest.TestCase (due to DB-incapsulations/Transactions/Rolbacks) ! see https://docs.djangoproject.com/en/4.2/topics/testing/overview/
    - Using unittest.TestCase avoids the cost of running each test in a transaction and flushing the database, but if your tests interact with the database their behavior will vary based on the order that the test runner executes them.

    --- run tests:
    - ! https://docs.djangoproject.com/en/4.2/topics/testing/overview/#running-tests
    - run-tests:  python manage.py test [dir1 /OR pkg1 /OR okg1.mod1.class1.method1 /OR .... ]  ##--: Test discovery is based on the unittest module’s built-in test discovery. By default, this will discover tests in any file named test*.py under the current working directory.
    - ! CTRL-C (one-time)  : clean-interrupt-tests (current test will complete and then exit gracefully)!
    - ! CTRL-C (two-times) : NOT-clean-interrupt-tests : the test run will halt immediately, but not gracefully ! and any test databases created by the run will NOT be destroyed ... !

    --- test-tools-- django.test:
    - ! https://docs.djangoproject.com/en/4.2/topics/testing/tools/
    --  test client :  
        - is a Python class that acts as a dummy web browser ...!
        - does NOT require a running webserver!! it goes directly to the api !
        - NOT a replacement for Selenium /OR urllib !! for Selenium see  LiveServerTestCase usage...!

    --- fixtures dor DB:
    - ! https://docs.djangoproject.com/en/4.2/topics/testing/tools/#fixture-loading

    --- selenium-dj / web-interface-Interactions-testings with dj-apps:
    - ! see : https://docs.djangoproject.com/en/4.2/intro/tutorial05/#further-testing
    - use  LiveServerTestCase  :
    - https://docs.djangoproject.com/en/4.2/topics/testing/tools/#django.test.LiveServerTestCase
    - https://docs.djangoproject.com/en/4.2/topics/testing/tools/
    - https://selenium-python.readthedocs.io/api.html
    - https://pypi.org/project/selenium/
    - ! Django includes LiveServerTestCase to facilitate integration with tools like Selenium.
    
    ---
    - pytest plugin django !
##________________________________________  ___________________________

