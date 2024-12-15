from django.shortcuts import render

# Create your views here.
def index(request):
    context1 = {"var1": "val-1", "var2": "val-2", "lis1": [10,11,12,13], "dic1": {"aa": 21, "bb": 22},}
    return render(request, "ap1/index.html", context1)
