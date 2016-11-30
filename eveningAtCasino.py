eveningAtCasino/
	__init__.py
	gamble/
			__init__.py
			gamble.py

def eveningAtCasino():
	lst = []
	flips = input("Enter an amount of flips: ")
	int_flips = int(flips)
	heads = input("Enter the anticipated amount of heads: ")
	int_heads = int(heads)
	profit = input("Enter the profit earned: ")
	int_profit = int(profit)
	lst.append(int_flips)
	lst.append(int_heads)
	lst.append(int_profit)
    for g in lst:
        g_stats = print(casino(g))
eveningAtCasino()