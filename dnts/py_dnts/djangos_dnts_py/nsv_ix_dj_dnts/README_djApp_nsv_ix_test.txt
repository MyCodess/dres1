

#####  ==========  ?? 2chat:
	- db-creation / reuse/ avoid-creation,... ! this runs <--> later !? conftest.py, ...!
##________________________________________  ___________________________


#####  ==========  2do/...:
	- params: global-params to tests/integration/params.py  (so eg. SMOKE from ixLib-params to global-params!)
##________________________________________  ___________________________


#####  ==========  
	- switch to venv; stay in project-root-dir (containing ./netservices/manage.py)
	- check that DJANGO_SETTINGS_MODULE env-var is set properly ! OR call: pytest --ds="netservices.settings.dev" ...
	- python -m pytest  --ds="netservices.settings.dev" -vv  --capture=no  -o cache_dir=/tmp/  ./tests/integration/netservices/

	=============== cmds-OK: ===========================
	--- pytest calls:
	python -m pytest  -vv  --capture=no  -o cache_dir=/tmp/  ./tests/integration/netservices/clients.py
	python -m pytest  -vv  --capture=no  -o cache_dir=/tmp/   --pyargs  tests.integration.netservices.clients  ##--same but as module/pkg ! use then --pyargs
	python -m pytest -o cache_dir=/tmp/   ./tests/integration/netservices/clients.py
	pytest -o cache_dir=/tmp/  ./tests/integration/netservices/clients.py

	--- manage.py / dj-shell calls:
	python -m manage test tests.integration.netservices.clients  ##--but no test-runs, since it is looking for unittest funcs! but the cmd works!
	python manage.py shell -c "exec(open('../tests/integration/netservices/clients.py').read())" ##-- BUT it does NOT run the main() ! since its __name__ is NOT __main__! see next section!
	--- ok-in-dj-shell:
	- OK in dj-shell on cmdline (must start in prj-root-dir, so that it finds tests....):
	(ve1) ~/ofc1/cod1/djix1/netservices : (feature/P10387-389-testing-infoblox-django-final):
	$ echo "import tests.integration.netservices.clients; tests.integration.netservices.clients.main()" | python -m manage shell
	- ! if __name__ == "__main__": is NOT True then ! so main() will NOT run  automatically!
	- and you must call as  python -m manage ... due to cu-dir in sys.path !
	=====================================================
##________________________________________  ___________________________


#####  ==========  more/1coll/djapp_ix_calls,...:
	$ python -m pytest  --ds="netservices.settings.dev" -v  --capture=no  -o cache_dir=/tmp/  ./tests/integration/netservices/core/views/infoblox/test_aaaa_records.py
##________________________________________  ___________________________

