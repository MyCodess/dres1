___________________________ asyncio , coroutines , async/wait_______________________________________


#####  ==========  docs:
	-! RefDocsStdLib-->Networking-->asyncio
	-! concept-explanation:   https://www.aeracode.org/2018/02/19/python-async-simplified/
	-! comprehensive/backgrounds:   https://realpython.com/async-io-python/
	pydoc  asyncio
	pydoc  types  ##not type !  --->  CoroutineType = class coroutine(object)  : send()/close()/...
##________________________________________  ___________________________


#####  ==========  Allg assyncio nts:

	_______:  awaitable objects :
	-! an object is an awaitable object if it can be used in an await expression
	- awaitable objects : There are three main types of awaitable objects: coroutines, Tasks, and Futures.
	-! Tasks are used to schedule coroutines CONCURRENTLY (so, in parallel!).
##________________________________________  ___________________________


#####  ==========  tips:
	-!  PYTHONASYNCIODEBUG , man python: set to a non-empty string, enable the debug mode of the asyncio module
##________________________________________  ___________________________


#####  ==========  coroutines / async def()... :

	_______:  urls/docs:
	https://peps.python.org/pep-0492/
	RefDocsLibs--Coroutines and Tasks  : https://docs.python.org/3.7/library/asyncio-task.html
	RefDocsRef--3.4 Coroutines  + RefDocsRef--8.8. Coroutines : https://docs.python.org/3.7/reference/compound_stmts.html#coroutines
	--
	https://tenthousandmeters.com/blog/python-behind-the-scenes-12-how-asyncawait-works-in-python/  ##--VERY comprehensive, from ground-up incl. theoriticals ...!
	https://www.geeksforgeeks.org/coroutine-in-python/

	_______:  -
	-!! Note that simply calling a coroutine will not schedule it to be executed (as main1()) !! but only by asyncio-calls will execute the coroutine, as: asyncio.run(main1()) /OR asyncio.gather(main1()), ...
	To actually run a coroutine (a func containing await), asyncio provides three main mechanisms: 
	1- asyncio.run(main()) , 2- asyncio.create_task(main1()) and then asyncio.run the tasks , 3-Awaiting on a coroutine (not-parallel); -2.b-and collect-variation: awaitable asyncio.gather(*mains)
	see pydocs-var/0Refs_HTMLs_py/library/asyncio-task.html  / 3.10.4 Documentation » The Python Standard Library » Networking and Interprocess Communication » asyncio — Asynchronous I/O » Coroutines and Tasks
##________________________________________  ___________________________


#####  ==========  ASGI :
	https://asgi.readthedocs.io/en/latest/introduction.html
##________________________________________  ___________________________


#####  ==========  Starlette : ASGI framework :
        https://www.starlette.io
        Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python.
##________________________________________  ___________________________

