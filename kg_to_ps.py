"""Write a program that asks the user for weight in kilograms
and converts it to pounds. There are 2.2 pounds in a kilogram"""

print("Convert(only integer) kilograms to pounds: ")
user_input = float(input("Write Kg"))
result = user_input * 2.2
print("The %.2f pounds!" % result)


input()
