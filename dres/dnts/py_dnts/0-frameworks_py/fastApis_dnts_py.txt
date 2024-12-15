____________________ FastAPI-prj1-try : /_230121  :  ________________________________________
- based on:   https://realpython.com/fastapi-python-web-apis/  /_230131  :
##________________________________________  ___________________________


#####  ==========  

	_______:  -- installl fastapi as u1 (not on system): 2023-01-21T13:26:32 CET
[u1@2209arx ~]$ python -m pip install fastapi "uvicorn[standard]"
...

	_______:  sending POST-data by ca,,ing a URL/Webpage/sending-request:
- browser:  /doc of the app as http://127.0.0.1:8000/docs
-!! cmdline/curl:  sending POST-data with curl/cmdline (see /doc protocol! ):  curl -v -X 'POST'   'http://127.0.0.1:8000/items/'   -H 'accept: application/json'   -H 'Content-Type: application/json'   -d '{ "name": "n1", "description": "desc1", "price":  1, "tax": 1 }'
- Postman :  https://www.postman.com/
: You could verify it by going to the same API documentation at /docs or by using other tools like Postman with a graphical interface or Curl in the command line. #/realPy-guide

	_______:  -- coll:
$ uvicorn main:app --reload
docs /openAPI :  http://127.0.0.1:8000/docs  mit Swagger UI  , bzw.  http://127.0.0.1:8000/redoc  
