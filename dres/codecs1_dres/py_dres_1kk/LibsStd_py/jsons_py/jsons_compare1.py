import json

d1 = {"k1": 11, "k2": 22}
d2 = {"k2": 22, "k1": 11}
assert d1 == d2



l1 = [
        {'_ref': 'record:a/ZG5aL', 'ipv4addr': '185.60.96.121', 'name': 'name1', 'view': 'view1'},
        {'_ref': 'record:a/ZG5bL', 'ipv4addr': '185.60.97.122', 'name': 'name2', 'view': 'view2'},
        {'_ref': 'record:a/ZG5cL', 'ipv4addr': '185.60.96.123', 'name': 'name3', 'view': 'view3'},
    ]


l2 = [
        {'_ref': 'record:a/ZG5aL', 'name': 'name1', 'view': 'view1', 'ipv4addr': '185.60.96.121'},
        {'_ref': 'record:a/ZG5bL', 'ipv4addr': '185.60.97.122', 'name': 'name2', 'view': 'view2'},
        {'_ref': 'record:a/ZG5cL', 'ipv4addr': '185.60.96.123', 'name': 'name3', 'view': 'view3'},
    ]

assert l1 == l2
