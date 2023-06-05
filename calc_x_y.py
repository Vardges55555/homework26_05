"""Write a program that asks the user to enter two numbers
, x, and y, and computes | x − y | /  x+y."""

x, y = float(input("Write first number(x): ")), float(input("Write second number(y): "))
result = abs(x-y) / (x + y)
print(round(result, 3))

input()
