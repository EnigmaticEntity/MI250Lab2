import random
def flipCoin():
    random.randrange(0,2)
    if random.randrange(0,2) == 0:
        print("Heads")
    else:
        print("Tails")

def casino(dollars):
	stats = []
    flips = 0
	heads = 0
    profit = 0
    while dollars >= 1 | flips < 300:
        dollars = dollars - 1
        random.randrange(0,2)
        if random.randrange(0,2) == 0:
            dollars = dollars + 1.2
            print("You won this flip, total is $" + str(dollars))
        else:
            print("Lost this flip")
