
def read(filename):
    """ read a text file and return a list of numbers """
    with open(filename) as f:
        lines = f.readlines()
        return [float(line) for line in lines]

def calculate_total(filename):
    """ return the sum of numbers in a text file """
    numbers = read(filename)
    return sum(numbers)

## print(read("f1.txt"))
## print(calculate_total("f1.txt"))

