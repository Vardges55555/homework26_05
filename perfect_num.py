"""A number is called a perfect number if it is equal to the sum of all of its divisors,
not including the number itself. For instance,
6 is a perfect number because the divisors of 6 are 1, 2, 3, 6, and 6 = 1 + 2 + 3.
As another example, 28 is a perfect number because its divisors are 1, 2, 4, 7,14, 28,
and 28=1+2+4+7+14. However,15 is not a perfect number because its divisors are 1, 3, 5, 15,
and 15 != 1 + 3 + 5. Write a program that finds all four of the perfect numbers
that are less than 10000.
"""

"""Число называется совершенным числом,
если оно равно сумме всех своих делителей, не считая самого числа.
Например, 6 — совершенное число, потому что делители 6 равны 1, 2, 3, 6, а 6 = 1 + 2 + 3.
Другой пример: 28 — совершенное число,
потому что его делители равны 1, 2, 4, 7,14, 28 и 28=1+2+4+7+14.
Однако 15 не является совершенным числом,
поскольку его делители равны 1, 3, 5, 15 и 15 != 1 + 3 + 5.
Напишите программу, которая находит все четыре совершенных числа, меньшие 10000."""

perfect_numbers = []

for num in range(2, 10001):
    sum_of_divisors = 1

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i

    if sum_of_divisors == num:
        perfect_numbers.append(num)

print("Perfect numbers up to 10000:")
for number in perfect_numbers:
    print(number)
