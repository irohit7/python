"""#45 * 3 = 555, 56+9 = 77, 56/6 = 4
print("Enter 1st Number")
num1 = int(input())
print('Enter 2nd Number')
num2 = int(input())
print('so What you Want?'+'+,-,/,%,*')
num3 =input()

if num1 ==45 and num2==3 and num3=='*':
    print("154")
elif num1 == 56 and num2 == 9 and num3 == '+':
        print("67")
elif num1 == 56 and num2 == 6 and num3 == '/':
        print("4")
elif num3=='*' :
    num4=num1*num2
    print(num4)
elif num3 == '+':
    plus=num2+num1
    print(plus)
elif num3 == '/':
    Dev=num2/num1
    print(Dev)
elif num3 == '%':
    percent=num2%num1
    print(percent)
else:
    print('Out Of Range') """

#45 * 3 = 555, 56+9 = 77, 56/6 = 4
num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))
print("Choose the arithmatic"+"+,-,*,/")
operand = input()
if num1 == 45 and num2 == 3 and operand == "*":
    print("555")
elif num1 == 56 and num2 == 9 and operand == "+":
    print("77")
elif num1 == 56 and num2 == 6 and operand == "/":
    print("4")
elif operand == "+":
    print(num1+num2)
elif operand == "-":
    print(num1-num2)
elif operand == "*":
    print(num1*num2)
elif operand == "/":
    print(num1/num2)
else:
    print("out of Range")