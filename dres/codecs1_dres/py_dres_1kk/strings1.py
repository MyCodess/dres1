# -- pydoc str :

s1 = "aa bb cc dd 11 22 33 44 AA BB CC DD"
print("- s1 :         ", s1)
print("- capitalize:  ", s1.capitalize())
print("- casefold  :  ", s1.casefold())
print("- center    :  ", s1.center(80, "-"))
print("- count     :  ", s1.count("b"))
print("- endswith  :  ", s1.endswith("b"))
print("- find      :  ", s1.find("bb"))
print("- index     :  ", s1.index("bb"))
print("- isalnum   :  ", s1.isalnum())
print("- join-1    :  ", "-+".join(s1))
print("- join-2    :  ", "-+".join(['ab', 'pq', 'rs']))
print("- replace-1 :  ", s1.replace("b", "X"))
print("- replace-2 :  ", s1.replace("b", "X", 1))  # -count=1

