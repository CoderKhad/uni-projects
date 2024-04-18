import random

def write_random_numbers(num_count):
    with open('random_numbers.txt', 'w') as f:
        for i in range(num_count):
            random_num = random.randint(1, 500)
            f.write(str(random_num) + '\n')

num_count = int(input("Enter the number of random numbers: "))
write_random_numbers(num_count)

def read_random_numbers():
    with open('random_numbers.txt', 'r') as f:
        numbers = [int(line.strip()) for line in f]
    
    total = sum(numbers)
    num_count = len(numbers)
    
    print("Random Numbers:")
    for num in numbers:
        print(num)
    
    print(f"Total: {total}")
    print(f"Number of Random Numbers: {num_count}")

read_random_numbers()
