# see:  https://python3.info/advanced/generator/expression.html
# - add print(result); os so, anywhere you want to see the result ...!

data = (1, 2, 3, 4)

result = (x for x in data)          # generator expression
print(next(result)); print(next(result)); print(next(result)); print(next(result));

result = [x for x in data]          # list comprehension
result = {x for x in data}          # set comprehension
result = {x:x for x in data}        # dict comprehension

result = tuple(x for x in data)     # tuple comprehension
result = list(x for x in data)      # list comprehension
result = set(x for x in data)       # set comprehension
result = dict((x,x) for x in data)  # dict comprehension

result = bool(x for x in data)
result = str(x for x in data)
result = all(x for x in data)
result = any(x for x in data)
result = sum(x for x in data)
result = min(x for x in data)
result = max(x for x in data)
result = hash(x for x in data)
result = callable(x for x in data)


