from unittest import mock

mk1 = mock.MagicMock()

def do_something(o):
    return o.f1("aa")
print (do_something(mk1))

mk1.f1.return_value = 11
print (do_something(mk1))
