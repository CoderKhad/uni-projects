import random

numbers = []
odd_count = 0
even_count = 0

for i in range(100):
	num = random.randint(0, 100)
	numbers.append(num)
	if num % 2 == 1:
		odd_count += 1
	else:
		even_count += 1

print("Random numbers:", numbers)
print("Odd numbers:", odd_count)
print("Even numbers:", even_count)
