"""A year is a leap year if it is divisible by 4,
except that years divisible by 100 are not leap years unless they are also divisible
by 400. Ask the user to enter a year, and, using the // operator,
determine how many leap years there have been between 1600 and that year."""

"""Год является високосным, если он делится на 4,
за исключением того, что годы, которые делятся на 100, не являются високосными,
если только они также не делятся на 400. Попросите пользователя ввести год и,
используя оператор //,определите, сколько високосные годы были между 1600 и этим годом."""

year = int(input("Write year: "))

leap_years = 0

for y in range(1600, year):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        leap_years += 1

print("days before 1600 ", year, "is", leap_years)
