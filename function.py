
# #task 1 create calculater using function

def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b
    else:
        return "Invalid operation"

print(calculate(10, 5, "add")) 
print(calculate(10, 5, "mul"))

# #task 2 create a function to check if a number is even or odd
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "odd"
number = int(input("Enter a number:"))
result = even_odd(number)
print("the number is",result)
# print(even_odd(7))

#task3 create a funtion to find a factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact* i
    return fact


num = 7
print(factorial(num))

#task 4 create a function to find maximum of three
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

result = find_max(num1, num2, num3)
print("Maximum number is:", result)

#task 5 create the function to check if a string is pallindrom
input_str = "madam"
def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]

input_str = input("Enter a string: ")

if is_palindrome(input_str):
    print("It is a palindrome")
else:
    print("Not a palindrome")

#task6 create a function to calculate area of circle
def areaofcircle(radius):
    pi = 3.14
    return pi * radius * radius

r = float(input("Enter radius of the circle: "))

area = areaofcircle(r)

print("Area of circle is:", area)

