from pprint import pprint

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings



#####  ==========  /:250803 :  settings-attribs/-params-listing OL/web : ====================
def settings1(request):
    sets1 = "----------------------------- settings-dict : ----------------------<br>"
    # -ok--not-sorted:  for ii in settings.__dict__: sets1 = f"{sets1}<br>{ii}   ::   {settings.__dict__[ii]}"
    for k, v in sorted(settings.__dict__.items()): sets1 = f"{sets1}<br>{k}   ::   {v}"
    sets1 += "----------------------------- settings-DIR : ----------------------<br>"
    for k in sorted(dir(settings)): sets1 = f"{sets1}<br>{k}<br>"
    return HttpResponse(f"Home-Index-netserv1,<p>- BASE_DIR:  {settings.BASE_DIR}<p>{sets1}")
##________________________________________  ___________________________

def index(request):
    return HttpResponse(f"Home1")
