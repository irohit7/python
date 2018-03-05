import math
num1 = input('Enter a>')
num2 = input('enter b>')
num3 = input('enter c>')
p    = (num1+num2+num3)/2
area = math.sqrt(p*(p-num1)*(p-num2)*(p-num3))

print ('the area of triangle is {0} {1} {2} {3}and is {4}'.format(num1,num2,num3,p,area))
