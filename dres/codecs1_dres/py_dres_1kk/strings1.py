# -- see Py3/Doc/html/library/string.html  bzw.  pydoc string , pydoc str :

############################## str methods (not string): #################
print('\n', '{0:=^78}'.format(" str methods: "))
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


##########################################################################
print('\n', '{0:=^78}'.format(" align padded text: "))
s2 = "test text words"
print('{0:-^78}'.format(" centred str ^ , padded with - , length of 78 total "))
print('{0:->78}'.format(" right-aligned str > , padded with - , length of 78 total "))
print('{0:-<78}'.format(" left-aligned str < , padded with - , length of 78 total "))

# =====================
print()
print("- Using the comma as a thousands separator:  ", '{:,}'.format(1234567890))
print("- Expressing a percentage:  ",  '{:.2%}'.format(42/92))

############################## templates: ################################
print('\n', '{0:=^78}'.format(" templates: "))
from string import Template
s = Template('$who likes $what')
print(s.substitute(who='tim', what='kung fu'))
# with dict :
d = dict(who='tim')
print(Template('Give $who ').substitute(d))
# -2try: excp:  print(Template('Give $who $100').substitute(d))
print(Template('$who likes $what').safe_substitute(d))

print()
