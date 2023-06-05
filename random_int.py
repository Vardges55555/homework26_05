"""Write a program that generates and prints 50 random integers,
each between 3 and 6."""
import random

for elm in range(50):
    rand_num = random.randint(3, 6)
    print(rand_num)


input()

