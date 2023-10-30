from unittest import mock

regular = mock.MagicMock()

def do_something(o):
    return o.f1("aa")

print (do_something(regular))

