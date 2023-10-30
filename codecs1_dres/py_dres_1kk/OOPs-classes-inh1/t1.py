cities = ["Berlin", "Vienna", "Zurich"]
iterator_obj = iter(cities)
print(iterator_obj)
print(iterator_obj.__next__())
print("---")
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))

