import random

lottery_number = [random.randint(0, 9) for _ in range(7)]

for digit in lottery_number:
	print(digit, end="")

print()  
