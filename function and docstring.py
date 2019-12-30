"""def function():
    print("This is function ")
print(function())  """

"""
def sum(a,b):
    c = a+b
    print(c)
    return c

a = int(input())
b = int(input())
sum(a,b)  """
"""
def average(a,b):
   #doc astring
    c = (a+b)/2
    print(c)

print(average.__doc__)
average(5,7)  """

#calculator using function

def sum(a,b):
    c = a+b
    print(c)
def minus(a,b):
    c = a-b
    print(c)
def mul(a,b):
    c = a*b
    print(c)
def div(a,b):
    c = a/b
    print(c)

a = int(input("Enter the 1st Number -> "))
b = int(input("Enter the 2nd Number -> "))
operand = input("Which operand you want to perform +,-,*,/  -> ")
if operand == "+":
    sum(a,b);
if operand == "-":
    min(a,b);
if operand == "*":
    mul(a,b);
if operand == "/":
    div(a,b);










