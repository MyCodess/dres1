
class C1():

    def __init__(self, ii: int):
        print(f"--- init: {ii}")

    def __call__(self, ii: int):
        print(f"--- call: {ii}")

def main1():
    o1 = C1(1)
    o1(21)

if __name__ == "__main__": main1()

